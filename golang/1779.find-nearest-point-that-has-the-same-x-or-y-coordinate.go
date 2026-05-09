func nearestValidPoint(x int, y int, points [][]int) int {
	idx := -1
	minDist := math.MaxInt

	for i, p := range points {
		if x == p[0] || y == p[1] {
			d := __dist(x, y, p[0], p[1])
			if d < minDist {
				idx = i
				minDist = d
			}
		}
	}

	return idx
}

func __dist(x, y, x0, y0 int) int {
	if x < x0 {
		x, x0 = x0, x
	}

	if y < y0 {
		y, y0 = y0, y
	}

	return x - x0 + y - y0
}
