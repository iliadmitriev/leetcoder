func robotSim(commands []int, obstacles [][]int) int {
	x, y := 0, 0
	dx, dy := 0, 1

	obs := make(map[[2]int]bool)
	for i := range obstacles {
		obs[[2]int(obstacles[i])] = true
	}

	farest := 0

	for _, cmd := range commands {
		if cmd == -1 {
			dx, dy = dy, -dx
		} else if cmd == -2 {
			dx, dy = -dy, dx
		} else {
			for ; cmd > 0; cmd-- {
				nx, ny := x+dx, y+dy
				if _, ok := obs[[2]int{nx, ny}]; ok {
					break
				}

				x, y = nx, ny
			}
		}

		farest = max(farest, x*x+y*y)
	}

	return farest
}
