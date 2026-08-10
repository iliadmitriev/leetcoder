func winnerSquareGame(n int) bool {
	dp := make([]bool, n+1)

	for i := range n + 1 {
		if dp[i] {
			continue // cached
		}

		for j := 1; i+j*j <= n; j++ {
			dp[i+j*j] = true
		}
	}

	return dp[n]
}