
const MOD = int(1e9) + 7

func productQueries(n int, queries [][]int) []int {
	pre := make([]int, 0)

	for n > 0 {
		b := n & -n
		pre = append(pre, b)
		n ^= b
	}

	// cache
	m := len(pre)
	cache := make([][]int, m)
	for i := range m {
		cache[i] = make([]int, m)
		cache[i][i] = pre[i]

		for j := i + 1; j < m; j++ {
			cache[i][j] = cache[i][j-1] * pre[j] % MOD
		}
	}

	// count
	res := make([]int, len(queries))
	for i, q := range queries {
		res[i] = cache[q[0]][q[1]]
	}

	return res
}
