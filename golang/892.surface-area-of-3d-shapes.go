func surfaceArea(grid [][]int) int {
	area := 0

	m, n := len(grid), len(grid[0])

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {

			// 4 tiles for 1 unit of height to cover whole column around
			area += grid[i][j] * 4

			// 2 tiles to cover the top and bottom
			if grid[i][j] > 0 {
				area += 2
			}

			// discard 2 tiles to for every unit of height of attachment
			// between two columns horizontally
			if i > 0 {
				area -= min(grid[i][j], grid[i-1][j]) * 2
			}

			// discard 2 tiles to 1 unit of height of attachment vertically
			if j > 0 {
				area -= min(grid[i][j], grid[i][j-1]) * 2
			}
		}
	}

	return area
}
