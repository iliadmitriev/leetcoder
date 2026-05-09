func countSquares(matrix [][]int) int {
	m, n := len(matrix), len(matrix[0])

	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 1 {
				dp[i+1][j+1] = 1 + min(dp[i][j], min(dp[i][j+1], dp[i+1][j]))
			}
		}
	}

	count := 0
	for i := 0; i <= m; i++ {
		for j := 0; j <= n; j++ {
			count += dp[i][j]
		}
	}
	return count
}
