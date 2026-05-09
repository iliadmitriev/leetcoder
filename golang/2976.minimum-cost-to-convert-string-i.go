func minimumCost(source string, target string, original []byte, changed []byte, cost []int) int64 {
	const (
		INF = int(-1)
		N   = 26
		A   = 'a'
	)

	dp := make([][]int, N)
	for i := range dp {
		dp[i] = make([]int, N)
		for j := range dp[i] {
			dp[i][j] = INF
		}

		dp[i][i] = 0
	}

	for i := range original {
    cur := dp[original[i]-A][changed[i]-A]
		if cur != INF && cur < cost[i] {
			continue
		}

		dp[original[i]-A][changed[i]-A] = cost[i]
	}

	for k := 0; k < N; k++ {
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
        if dp[i][k] == INF || dp[k][j] == INF {
          continue
        }

				path := dp[i][k] + dp[k][j]
				if dp[i][j] != INF && dp[i][j] < path {
					continue
				}

				dp[i][j] = path
			}
		}
	}

	total := 0

	for i := range source {
		if dp[source[i]-A][target[i]-A] == INF {
			return -1
		}

		total += dp[source[i]-A][target[i]-A]
	}

	return int64(total)
}
