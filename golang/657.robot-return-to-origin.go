func judgeCircle(moves string) bool {
	x, y := 0, 0
	for _, m := range moves {
		switch m {
		case 'U':
			y++
		case 'D':
			y--
		case 'L':
			x--
		case 'R':
			x++
		}
	}

	return x == 0 && y == 0
}