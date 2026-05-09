func numberOfLines(widths []int, s string) []int {
	const pixLimit = 100

	lines := 1
	pixels := 0

	for i := 0; i < len(s); i++ {
		if pixels+widths[s[i]-'a'] > pixLimit {
			lines++
			pixels = 0
		}

		pixels += widths[s[i]-'a']
	}

	return []int{lines, pixels}
}
