func closedIsland(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	res := 0

	var dfs_fill func(int, int) bool
	dfs_fill = func(r, c int) bool {
		if r < 0 || c < 0 || r >= m || c >= n {
			return false
		}

		if grid[r][c] == 1 {
			return true
		}

		grid[r][c] = 1 // mark

		up := dfs_fill(r+1, c)
		right := dfs_fill(r, c+1)
		down := dfs_fill(r-1, c)
		left := dfs_fill(r, c-1)

		return up && right && down && left
	}

	for r := range m {
		for c := range n {
			if grid[r][c] == 0 && dfs_fill(r, c) {
				res++
			}
		}
	}

	return res
}