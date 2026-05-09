import "strings"

func mostWordsFound(sentences []string) int {
	maxWords := 0

	for i := 0; i < len(sentences); i++ {
		maxWords = max(maxWords, len(strings.Split(sentences[i], " ")))
	}

	return maxWords
}
