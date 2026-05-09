func findColumnWidth(grid [][]int) []int {
	m, n := len(grid), len(grid[0])

	res := make([]int, n)

	for j := 0; j < n; j++ {
		maxLen := 0
		curLen := 0

		for i := 0; i < m; i++ {

			curLen = 0
			x := grid[i][j]
			if x <= 0 {
				curLen++
				x = -x
			}

			for x > 0 {
				curLen++
				x /= 10
			}

			if curLen > maxLen {
				maxLen = curLen
			}
		}

		res[j] = maxLen
	}

	return res

}
