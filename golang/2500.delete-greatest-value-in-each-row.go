func deleteGreatestValue(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	for i := 0; i < m; i++ {
		sort.Ints(grid[i])
	}

	res := 0

	for j := 0; j < n; j++ {
		maxRow := grid[0][j]
		for i := 1; i < m; i++ {
			maxRow = max(maxRow, grid[i][j])
		}

		res += maxRow
	}

	return res
}
