func mostPoints(questions [][]int) int64 {
	n := len(questions)
	dp := make([]int, n+1)

	for i := n - 1; i >= 0; i-- {
		points, brainpower := questions[i][0], questions[i][1]

		next := min(n, i+brainpower+1)
		dp[i] = max(dp[i+1], points+dp[next])
	}

	return int64(dp[0])
}
