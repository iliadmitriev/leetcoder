func numberOfSpecialChars(word string) int {
	lower := [26]int{}
	upper := [26]int{}
	count := 0

	for i := range 26 {
		upper[i] = -1
		lower[i] = -1
	}

	for i := range len(word) {
		ch := word[i]

		if 'a' <= ch && ch <= 'z' {
			lower[ch-'a'] = i + 1
		} else if upper[ch-'A'] == -1 {
			upper[ch-'A'] = i + 1
		}
	}

	for i := range 26 {
		if lower[i] > 0 && lower[i] < upper[i] {
			count++
		}
	}

	return count
}