const MOD = int(1e9 + 7)

func numWays(words []string, target string) int {
	m, n, p := len(words[0]), len(target), len(words)

	wc := make([][]int, m)
	for j := range wc {
		wc[j] = make([]int, 26)
	}

	for j := 0; j < m; j++ {
		for k := 0; k < p; k++ {
			wc[j][words[k][j]-'a']++
		}
	}

	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
	}

	for j := m; j >= 0; j-- {
		dp[n][j] = 1
	}

	// m - wc pos j
	// n - target pos i

	for i := n - 1; i >= 0; i-- {
		for j := m - 1; j >= 0; j-- {

			ways := 0

			if wc[j][target[i]-'a'] > 0 {
				ways += dp[i+1][j+1] * wc[j][target[i]-'a']
				ways %= MOD
			}

			ways += dp[i][j+1]
			ways %= MOD
			dp[i][j] = ways
		}
	}

	return dp[0][0]
}
