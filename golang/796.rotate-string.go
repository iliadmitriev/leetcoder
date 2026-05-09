func rotateString(s string, goal string) bool {
	for i := 0; i < len(s); i++ {
		if goal == s[i:]+s[:i] {
			return true
		}
	}

	return false
}
