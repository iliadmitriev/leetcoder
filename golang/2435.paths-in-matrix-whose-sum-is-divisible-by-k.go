func numberOfPaths(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])
	const MOD = int(1e9) + 7

	dp := make([][]int, n+1)
	for c := range dp {
		dp[c] = make([]int, k)
	}

	// base state for forst columnt and 0 remainder
	dp[1][0] = 1

	for r := range m {
		for c := range n {
			row := make([]int, k)

			for rem := range k {
				nextRem := (rem + grid[r][c]) % k

				row[rem] = (dp[c+1][nextRem] + dp[c][nextRem]) % MOD
			}

			dp[c+1] = row
		}
	}

	return dp[n][0]
}
