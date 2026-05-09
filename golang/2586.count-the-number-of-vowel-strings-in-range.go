func vowelStrings(words []string, left int, right int) int {
	counter := 0

	for i := left; i <= right; i++ {
		if engVowelCheck(words[i][0]) && engVowelCheck(words[i][len(words[i])-1]) {
			counter++
		}
	}

	return counter
}

func engVowelCheck(b byte) bool {
	return b == 'a' || b == 'e' || b == 'i' || b == 'o' || b == 'u'
}
