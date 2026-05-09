func numberOfPairs(points [][]int) int {
	count := 0
	n := len(points)

	slices.SortFunc(points, func(a, b []int) int {
		if a[0] == b[0] {
			return b[1] - a[1]
		}

		return a[0] - b[0]
	})

	for i := range n {
		maxY := points[i][1]
		minY := math.MinInt

		for j := i + 1; j < n; j++ {
			if minY < points[j][1] && points[j][1] <= maxY {
				count++
				minY = points[j][1]
			}

			if maxY == minY {
				break
			}
		}
	}

	return count
}
