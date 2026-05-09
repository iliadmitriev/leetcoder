func countSegments(s string) int {
	seg := 0
	prev := rune(' ')

	// count transitions from space to non-space
	for _, ch := range s {
		if prev == ' ' && ch != ' ' {
			seg++
		}

		prev = ch
	}

	return seg
}
