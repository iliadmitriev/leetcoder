func findClosest(x int, y int, z int) int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	d1 := abs(x - z)
	d2 := abs(y - z)

	if d1 < d2 {
		return 1
	} else if d2 < d1 {
		return 2
	}

	return 0
}
