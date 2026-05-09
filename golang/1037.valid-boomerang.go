func isBoomerang(points [][]int) bool {
	x1, y1, x2, y2 := points[0][0], points[0][1], points[1][0], points[1][1]
	x3, y3 := points[2][0], points[2][1]

	// if x coordinates the same then points are on the same vertical line
	if x1 == x2 && x2 == x3 {
		return false
	}

	// if y coordinates the same then points are on the same horizontal line
	if y1 == y2 && y2 == y3 {
		return false
	}

	// x2 - x1 / y2 - y1 = x3 - x1 / y3 - y1
	// x2 - x1 * y3 - y1 = x3 - x1 * y2 - y1

	return (x2-x1)*(y3-y1) != (x3-x1)*(y2-y1)
}
