func numberOfWays(n int, x int) int {
	dp := newDpNumWays(n, x)
	return dp.dp(n, 1)
}

type dpNumWays struct {
	cache [][]int
	limit int
	order int
}

func newDpNumWays(n int, order int) *dpNumWays {
	limit := int(math.Pow(float64(n), 1.0/float64(order))) + 1

	cache := make([][]int, n+1)
	for i := range n + 1 {
		cache[i] = make([]int, limit+1)
		for j := range limit + 1 {
			cache[i][j] = -1
		}
	}

	return &dpNumWays{
		cache: cache,
		limit: limit,
		order: order,
	}
}

func (d *dpNumWays) dp(n, i int) int {
	if n == 0 {
		return 1
	}

	if n < 0 || i > d.limit {
		return 0
	}

	if d.cache[n][i] != -1 {
		return d.cache[n][i]
	}

	next := pow(i, d.order)
	d.cache[n][i] = d.dp(n-next, i+1) + d.dp(n, i+1)
	d.cache[n][i] %= 1000000007

	return d.cache[n][i]
}

// pow returns x^k
func pow(x, k int) int {
	res := 1
	base := x

	for k > 0 {
		if k%2 == 1 {
			res *= base
		}
		k >>= 1
		base *= base
	}

	return res
}
