func numberOfStableArrays(zero int, one int, limit int) int {
	const (
		MOD = int(1e9 + 7)
	)

	// dp[number of used zeros][number of used ones][last placed digit]
	dp := make([][][2]int, zero+1)
	for i := range zero + 1 {
		dp[i] = make([][2]int, one+1)
	}

	// initial values
	for i := 0; i <= min(zero, limit); i++ {
		dp[i][0][0] = 1
	}

	for j := 0; j <= min(one, limit); j++ {
		dp[0][j][1] = 1
	}

	// recurrence

	for i := 1; i <= zero; i++ {
		for j := 1; j <= one; j++ {
			// == try zero
			dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
			// cut off over limit + 1 (ones)
			if i > limit {
				dp[i][j][0] -= dp[i-limit-1][j][1]
			}
			// normilize
			dp[i][j][0] = (MOD + dp[i][j][0]%MOD) % MOD

			// == try one
			dp[i][j][1] = dp[i][j-1][0] + dp[i][j-1][1]
			// cut off over limit + 1 (zeros)
			if j > limit {
				dp[i][j][1] -= dp[i][j-limit-1][0]
			}
			// normalize
			dp[i][j][1] = (MOD + dp[i][j][1]%MOD) % MOD
		}
	}

	return (dp[zero][one][0] + dp[zero][one][1]) % MOD
}