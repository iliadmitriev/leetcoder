func truncateSentence(s string, k int) string {
	cut := len(s)
	words := 0

	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			words++
		}

		if words == k {
			cut = i
			break
		}
	}

	return s[:cut]
}
