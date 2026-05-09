func minimumMoves(s string) int {
	ops := 0
	for i := 0; i < len(s); {
		if s[i] == 'X' {
			i += 3
			ops++
		} else {
			i++
		}
	}

	return ops
}