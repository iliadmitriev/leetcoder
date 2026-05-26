func numberOfSpecialChars(word string) int {
	lower := make([]bool, 26)
	upper := make([]bool, 26)
	res := 0

	for i := range len(word) {
		ch := word[i]
		if 'a' <= ch && ch <= 'z' {
			lower[ch-'a'] = true
		} else {
			upper[ch-'A'] = true
		}
	}

	for i := range 26 {
		if upper[i] && lower[i] {
			res++
		}
	}

	return res
}