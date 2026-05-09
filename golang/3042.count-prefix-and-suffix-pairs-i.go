import "strings"

func countPrefixSuffixPairs(words []string) int {
	count := 0
	n := len(words)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if isSuffixAndPrefix(words[i], words[j]) {
				count++
			}
		}
	}

	return count
}

func isSuffixAndPrefix(suf, word string) bool {
	return strings.HasPrefix(word, suf) && strings.HasSuffix(word, suf)
}
