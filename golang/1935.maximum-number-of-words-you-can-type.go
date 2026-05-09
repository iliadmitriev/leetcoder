import "strings"

func canBeTypedWords(text string, brokenLetters string) int {
	count := 0
	for _, word := range strings.Split(text, " ") {
		if !strings.ContainsAny(word, brokenLetters) {
			count++
		}
	}

	return count
}
