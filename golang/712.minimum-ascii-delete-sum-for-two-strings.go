
func minimumDeleteSum(s1 string, s2 string) int {
	m, n := len(s1), len(s2)

	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	for i := m - 1; i >= 0; i-- {
		dp[i][n] = dp[i+1][n] + int(s1[i])
	}

	for j := n - 1; j >= 0; j-- {
		dp[m][j] = dp[m][j+1] + int(s2[j])
	}

	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if s1[i] == s2[j] {
				dp[i][j] = dp[i+1][j+1]
			} else {
				dp[i][j] = min(
					int(s1[i])+dp[i+1][j],
					int(s2[j])+dp[i][j+1],
				)
			}
		}
	}

	return dp[0][0]
}
