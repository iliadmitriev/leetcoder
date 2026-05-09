
func peopleAwareOfSecret(n int, delay int, forget int) int {
	const MOD int = 1e9 + 7

	dp := make([]int, n)
	dp[0] = 1
	s := 0

	for i := delay; i < n; i++ {
		s += dp[i-delay]
		dp[i] = s % MOD

		if i-forget+1 >= 0 {
			s -= dp[i-forget+1]
			s = (s + MOD) % MOD
		}
	}

	res := 0

	for i := n - forget; i < n; i++ {
		res = (res + dp[i]) % MOD
	}

	return res
}
