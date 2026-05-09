func findMinArrowShots(points [][]int) int {
	sort.Slice(points, func(i, j int) bool {
		return points[i][1] < points[j][1]
	})

	prevEnd := points[0][1]
	arrows := 1

	for _, point := range points {
		if point[0] > prevEnd {
			arrows++
			prevEnd = point[1]
		}
	}

	return arrows
}
