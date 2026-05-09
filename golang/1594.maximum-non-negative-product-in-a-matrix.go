func maxProductPath(grid [][]int) int {
	const MOD = int64(1e9) + 7

	m, n := len(grid), len(grid[0])

	dp := make([][][2]int64, m) // grid of pair[0 - min val, 1 - max val]
	for i := range m {
		dp[i] = make([][2]int64, n)
	}

	// init

	dp[0][0][0] = int64(grid[0][0]) // min
	dp[0][0][1] = int64(grid[0][0]) // max

	for i := 1; i < m; i++ {
		val := dp[i-1][0][0] * int64(grid[i][0])

		dp[i][0][0] = val // min
		dp[i][0][1] = val // max
	}

	for j := 1; j < n; j++ {
		val := dp[0][j-1][0] * int64(grid[0][j])

		dp[0][j][0] = val // min
		dp[0][j][1] = val // max
	}

	// search

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			minVal := min(dp[i][j-1][0], dp[i-1][j][0]) * int64(grid[i][j])
			maxVal := max(dp[i][j-1][1], dp[i-1][j][1]) * int64(grid[i][j])

			if grid[i][j] >= 0 {
				dp[i][j][0] = minVal
				dp[i][j][1] = maxVal
			} else {
				dp[i][j][0] = maxVal
				dp[i][j][1] = minVal
			}
		}
	}

	// if max value of final step is less than 0
	if dp[m-1][n-1][1] < 0 {
		return -1
	}

	// return max value of final step
	return int(dp[m-1][n-1][1] % MOD)
}