func finalPositionOfSnake(n int, commands []string) int {
	r, c := 0, 0

	for _, cmd := range commands {
		switch cmd[0] {
		case 'U':
			r--
		case 'D':
			r++
		case 'L':
			c--
		case 'R':
			c++
		}
	}

	return n*r + c
}
