func zigZagArrays(n int, l int, r int) int {
	const MOD = int(1e9) + 7
	m := r - l + 1

	dp0, dp1 := make([]int, m), make([]int, m)
	sum0, sum1 := make([]int, m+1), make([]int, m+1)

	for j := range m {
		dp0[j] = 1
		dp1[j] = 1 // base case
	}

	for i := 1; i < n; i++ {
		for j := range m {
			sum0[j+1] = (sum0[j] + dp0[j]) % MOD
			sum1[j+1] = (sum1[j] + dp1[j]) % MOD
		}

		for j := range m {
			dp0[j] = (sum1[m] - sum1[j+1] + MOD) % MOD
			dp1[j] = sum0[j]
		}
	}

	ans0, ans1 := 0, 0

	for j := range m {
		ans0 = (ans0 + dp0[j]) % MOD
		ans1 = (ans1 + dp1[j]) % MOD
	}

	return (ans0 + ans1) % MOD
}