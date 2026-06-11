func assignEdgeWeights(edges [][]int) int {
	const mod = int(1e9) + 7

	n := uint32(len(edges) + 2)
	adj := make([][]uint32, n)

	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], uint32(e[1]))
		adj[e[1]] = append(adj[e[1]], uint32(e[0]))
	}

	var dfs func(uint32, uint32) int
	dfs = func(u, parent uint32) int {
		d := 0
		for _, v := range adj[u] {
			if v == parent {
				continue
			}

			d = max(d, 1+dfs(v, u))
		}

		return d
	}

	k := dfs(1, 0) - 1

	// modular exponent 2^k
	// our target value 2^(k - 1) (k = level)
	res := 1
	base := 2
	for k > 0 {
		if k&1 == 1 {
			res *= base
			res %= mod
		}

		base *= base
		base %= mod
		k >>= 1
	}

	return res
}