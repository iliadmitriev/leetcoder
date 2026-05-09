
func findMaxForm(strs []string, m int, n int) int {
	l := len(strs)
	dp := make([][]int, m+1)

	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	for i := range l {
		zeros := strings.Count(strs[i], "0")
		ones := len(strs[i]) - zeros

		for j := m; j >= zeros; j-- {
			for k := n; k >= ones; k-- {
				dp[j][k] = max(dp[j][k], dp[j-zeros][k-ones]+1)
			}
		}
	}

	return dp[m][n]
}
