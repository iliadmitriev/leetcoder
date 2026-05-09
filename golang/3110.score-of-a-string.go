func scoreOfString(s string) int {
	score := 0

	for i := 1; i < len(s); i++ {
		score += absByte(s[i-1], s[i])
	}

	return score
}

func absByte(a, b byte) int {
	if a > b {
		return int(a - b)
	}
	return int(b - a)
}
