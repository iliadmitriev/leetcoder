func findMissingAndRepeatedValues(grid [][]int) []int {
	repeated, missing := 0, 0
	n := len(grid)
	seen := make([]int, n*n+1)

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if seen[grid[i][j]] == 1 {
				repeated = grid[i][j]
			}

			missing ^= grid[i][j] ^ (i*n + j + 1)
			seen[grid[i][j]]++
		}
	}

	return []int{repeated, missing ^ repeated}
}
