func isOneBitCharacter(bits []int) bool {

	n := len(bits)

	for i := 0; i < n; i += (1 + bits[i]) {
		if i == n-1 {
			return true
		}
	}

	return false
}
