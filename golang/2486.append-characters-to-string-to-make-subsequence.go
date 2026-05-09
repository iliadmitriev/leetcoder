func appendCharacters(s string, t string) int {
	n, m := len(s), len(t)
	j := 0

	for i := 0; i < n && j < m; i++ {
		if s[i] == t[j] {
			j++
		}
	}

	return m - j
}
