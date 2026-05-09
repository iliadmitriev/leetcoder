import (
	"strings"
	"unicode"
)

func mostCommonWord(paragraph string, banned []string) string {
	n := len(paragraph)
	bannedSet := make(map[string]bool, len(banned))

	for _, ban := range banned {
		bannedSet[strings.ToLower(ban)] = true
	}

	counts := make(map[string]int)

	for i, j := 0, 0; i < n; {
		for i < n && !unicode.IsLetter(rune(paragraph[i])) {
			i++
		}

		j = i

		for j < n && unicode.IsLetter(rune(paragraph[j])) {
			j++
		}

		if j > i && !bannedSet[strings.ToLower(paragraph[i:j])] {
			counts[strings.ToLower(paragraph[i:j])]++
		}

		i = j
	}

	maxWord := ""
	maxCount := 0

	for k, v := range counts {
		if v > maxCount {
			maxCount = v
			maxWord = k
		}
	}

	return maxWord
}
