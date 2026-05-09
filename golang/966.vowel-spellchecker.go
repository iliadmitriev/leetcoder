import (
	"strings"
)

func spellchecker(wordlist []string, queries []string) []string {
	n := len(wordlist)
	exact := make(map[string]struct{}, n)
	lower := make(map[string]int, n)
	vowel := make(map[string]int, n)

	for i, word := range wordlist {
		if _, ok := exact[word]; !ok {
			exact[word] = struct{}{}
		}

		lowered := strings.ToLower(word)

		if _, ok := lower[lowered]; !ok {
			lower[lowered] = i
		}

		vowelized := vowelize(word)
		if _, ok := vowel[vowelized]; !ok {
			vowel[vowelized] = i
		}
	}

	res := make([]string, 0, len(queries))

	for _, q := range queries {
		if _, ok := exact[q]; ok {
			res = append(res, q)
		} else if i, ok := lower[strings.ToLower(q)]; ok {
			res = append(res, wordlist[i])
		} else if i, ok := vowel[vowelize(q)]; ok {
			res = append(res, wordlist[i])
		} else {
			res = append(res, "")
		}
	}

	return res
}

func vowelize(s string) string {
	res := []byte(strings.ToLower(s))

	for i, ch := range res {
		if ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' {
			res[i] = 'a'
		}
	}

	return string(res)
}
