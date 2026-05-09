func minimumRecolors(blocks string, k int) int {
	count := k
	curWindow := 0

	for i := 0; i < len(string(blocks)); i++ {
		if blocks[i] == 'W' {
			curWindow++
		}

		if i >= k && blocks[i-k] == 'W' {
			curWindow--
		}

		if i >= k-1 && curWindow < count {
			count = curWindow
		}
	}

	return count
}
