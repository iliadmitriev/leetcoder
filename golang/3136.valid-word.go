import (
	"strings"
)

func isValid(word string) bool {
	if len(word) < 3 {
		return false
	}

	hasConsonant, hasVowel := false, false
	lower := strings.ToLower(word)

	for i := range len(word) {
		w := lower[i]

		if ('a' > w || w > 'z') && ('0' > w || w > '9') {
			return false
		}

		if !hasVowel && w == 'a' || w == 'e' || w == 'i' || w == 'o' || w == 'u' {
			hasVowel = true
		} else if !hasConsonant && w != 'a' && w != 'e' && w != 'i' && w != 'o' && w != 'u' && 'a' <= w && w <= 'z' {
			hasConsonant = true
		}
	}

	return hasConsonant && hasVowel
}
