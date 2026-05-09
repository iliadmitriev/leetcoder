func checkXMatrix(grid [][]int) bool {
	m, n := len(grid), len(grid[0])
	if m != n {
		return false
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if (i == j) || (n-i-1 == j) {
				if grid[i][j] == 0 {
					return false
				}
			} else {
				if grid[i][j] != 0 {
					return false
				}
			}
		}
	}

	return true
}
