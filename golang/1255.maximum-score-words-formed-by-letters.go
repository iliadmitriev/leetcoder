const alpaLen = 26

func checkWordFit(word string, letterMap []int) bool {
	wordMap := make([]int, alpaLen)
	for i := range word {
		wordMap[word[i]-97]++
	}
	for i := range wordMap {
		if letterMap[i] < wordMap[i] {
			return false
		}
	}

	return true
}

func countWordScore(word string, letterMap []int, scoreMap []int) int {
	score := 0
	for i := range word {
		score += scoreMap[word[i]-97]
		letterMap[word[i]-97]--
	}

	return score
}

func returnWordLetters(word string, letterMap []int) {
	for i := range word {
		letterMap[word[i]-97]++
	}
}

func dfsFindMaxScoreWords(words []string, letterMap []int, scoreMap []int, i, score int) int {
	if i == len(words) {
		return score
	}

	res := dfsFindMaxScoreWords(words, letterMap, scoreMap, i+1, score)
	if checkWordFit(words[i], letterMap) {
		currScore := countWordScore(words[i], letterMap, scoreMap)
		res = max(res, dfsFindMaxScoreWords(words, letterMap, scoreMap, i+1, score+currScore))
		returnWordLetters(words[i], letterMap)
	}

	return res
}

func maxScoreWords(words []string, letters []byte, score []int) int {
	letterMap := make([]int, alpaLen)
	for _, c := range letters {
		letterMap[c-97]++
	}

	return dfsFindMaxScoreWords(words, letterMap, score, 0, 0)
}
