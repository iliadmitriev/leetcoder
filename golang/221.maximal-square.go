func maximalSquare(matrix [][]byte) int {
	m, n := len(matrix), len(matrix[0])
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	ans := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == '0' {
				continue
			}

			dp[i][j] = int(matrix[i][j] - '0')

			if i > 0 && j > 0 {
				dp[i][j] += min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
			}

			ans = max(ans, dp[i][j])
		}
	}

	return ans * ans
}
