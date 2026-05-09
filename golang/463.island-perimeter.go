package main

func islandPerimeter(grid [][]int) int {
	res := 0

	m, n := len(grid), len(grid[0])

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 {
				continue
			}

			res += 4
			if i > 0 && grid[i-1][j] == 1 {
				res -= 2
			}
			if j > 0 && grid[i][j-1] == 1 {
				res -= 2
			}
		}
	}

	return res
}
