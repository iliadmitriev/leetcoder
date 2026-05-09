func minChanges(s string) int {
	counter := 0
	n := len(s)

	for i := 0; i < n; i += 2 {
		if s[i] != s[i+1] {
			counter++
		}
	}

	return counter
}