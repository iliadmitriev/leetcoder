func maxMoves(grid [][]int) int {
	maxMoves := 0
	m, n := len(grid), len(grid[0])

	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
		dp[i][0] = 1
	}

	for j := 1; j < n; j++ {
		for i := 0; i < m; i++ {
			if grid[i][j] > grid[i][j-1] && dp[i][j-1] > 0 {
				dp[i][j] = max(dp[i][j], dp[i][j-1]+1)
			}

			if i-1 >= 0 && grid[i][j] > grid[i-1][j-1] && dp[i-1][j-1] > 0 {
				dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
			}

			if i+1 < m && grid[i][j] > grid[i+1][j-1] && dp[i+1][j-1] > 0 {
				dp[i][j] = max(dp[i][j], dp[i+1][j-1]+1)
			}

			maxMoves = max(maxMoves, dp[i][j]-1)
		}
	}

	return maxMoves
}
