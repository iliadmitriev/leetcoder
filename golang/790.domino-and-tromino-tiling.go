const MOD = 1e9 + 7

func numTilings(n int) int {
	f, f1, f2, f3 := 1, 1, 1, 0

	for range n - 1 {
		f = (2*f1 + f3) % MOD
		f3 = f2
		f2 = f1
		f1 = f
	}

	return f
}
