func maxPoints(points [][]int) int64 {
	m, n := len(points), len(points[0])

	row := make([]int, n)
	copy(row, points[0])

	for i := 1; i < m; i++ {
		left := make([]int, n)
		left[0] = row[0]
		for j := 1; j < n; j++ {
			left[j] = max(row[j], left[j-1]-1)
		}

		right := make([]int, n)
		right[n-1] = row[n-1]
		for j := n - 2; j >= 0; j-- {
			right[j] = max(row[j], right[j+1]-1)
		}

		for j := 0; j < n; j++ {
			row[j] = max(left[j], right[j]) + points[i][j]
		}
	}

	res := row[0]
	for _, v := range row {
		res = max(res, v)
	}

	return int64(res)
}
