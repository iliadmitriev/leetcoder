
// expMod modular exponentiation.
func expMod(base, exp, mod int) int {
	res := 1

	for exp > 0 {
		if exp&1 == 1 {
			res *= base
			res %= mod
		}
		base *= base
		base %= mod
		exp >>= 1
	}

	return res
}

// invMod returns the modular inverse of a based on Euclidean algorithm
func invMod(n, mod int) int {
	res := expMod(n, mod-2, mod)
	return res
}

// factMod returns the modular factorial of n
func factMod(n, mod int) int {
	res := 1
	for i := 2; i <= n; i++ {
		res *= i
		res %= mod
	}
	return res
}

// combMod returns the modular combination of n choose k.
// C(n, k)! = n! * inv(k!) * inv(n-k)!
func combMod(n, k, mod int) int {
	f1 := factMod(n, mod)
	i2 := invMod(factMod(k, mod), mod)
	i3 := invMod(factMod(n-k, mod), mod)

	res := f1 * i2 % mod
	res = res * i3 % mod
	return res
}

func countGoodArrays(n int, m int, k int) int {
	const mod = int(1e9) + 7

	c := combMod(n-1, n-k-1, mod)
	return c * expMod(m-1, n-k-1, mod) % mod * m % mod
}
