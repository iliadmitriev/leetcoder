func getMaximumGenerated(n int) int {
	if n < 2 {
		return n
	}

	dp := make([]int, n+1)

	dp[0] = 0
	dp[1] = 1
	res := 1

	for i := 1; i <= n/2; i++ {
		dp[i*2] = dp[i]
		res = max(res, dp[i*2])

		if i*2+1 <= n {
			dp[i*2+1] = dp[i] + dp[i+1]
			res = max(res, dp[i*2+1])
		}
	}

	return res
}
