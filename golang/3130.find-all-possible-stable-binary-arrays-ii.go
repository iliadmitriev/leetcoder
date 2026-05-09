// func numberOfStableArrays(zero int, one int, limit int) int {

// }

const MOD = 1_000_000_007

func modinv(n int) int {
	x, y, px, py := 0, 1, 1, 0
	m := MOD
	for m != 0 {
		q := n / m
		n, m = m, n%m
		px, x = x, px-q*x
		py, y = y, py-q*y
	}
	return px
}

func ncr(n, r int) int {
	if r > n/2 {
		r = n - r
	}
	num, den := 1, 1
	for i := 1; i <= r; i++ {
		num = (num * (n - i + 1)) % MOD
		den = (den * i) % MOD
	}
	return (num * modinv(den)) % MOD
}

func splitways(n, k, limit int) int {
	if n == k {
		return 1
	}
	if n > k*limit {
		return 0
	}
	total, flag, remaining := 0, 1, n
	for j := 0; j <= k && k <= remaining; j++ {
		term := ncr(k, j) * ncr(remaining-1, k-1)
		total = (total + flag*term + MOD*MOD) % MOD
		flag = -flag
		remaining -= limit
	}
	return total
}

func numberOfStableArrays(zero, one, limit int) int {
	prev, curr, next := 0, splitways(one, 1, limit), splitways(one, 2, limit)
	result := 0
	for k := 1; k <= zero; k++ {
		choices := (prev + 2*curr + next) * splitways(zero, k, limit)
		result = (result + choices) % MOD
		prev, curr, next = curr, next, splitways(one, k+2, limit)
	}
	return result
}