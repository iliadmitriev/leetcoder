import "strings"

func isPrefixOfWord(sentence string, searchWord string) int {
	for pos, word := range strings.Split(sentence, " ") {
		if strings.HasPrefix(word, searchWord) {
			return pos + 1
		}
	}

	return -1
}
