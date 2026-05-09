func kthCharacter(k int) byte {
	n := 0

	for k--; k > 0; k &= k - 1 {
		n++
	}

	return 'a' + byte(n)
}
