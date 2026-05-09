func maximumAmount(coins [][]int) int {
	const negInf = -1 << 31

	m, n := len(coins), len(coins[0])
	memo := make([][][]int, m)
	for i := range memo {
		memo[i] = make([][]int, n)
		for j := range memo[i] {
			memo[i][j] = make([]int, 3)
			for k := range memo[i][j] {
				memo[i][j][k] = negInf
			}
		}
	}

	var dfs func(i, j, k int) int
	// i - row, j - col, k - spells left
	dfs = func(i, j, k int) int {
		if i >= m || j >= n {
			return negInf
		}

		x := coins[i][j]
		// arrive at the destination
		if i == m-1 && j == n-1 {
			if k > 0 {
				return max(0, x)
			}
			return x
		}

		if memo[i][j][k] != negInf {
			return memo[i][j][k]
		}

		// not neutralize
		res := x + max(dfs(i+1, j, k), dfs(i, j+1, k))
		if k > 0 && x < 0 {
			// neutralize
			res = max(res, max(dfs(i+1, j, k-1), dfs(i, j+1, k-1)))
		}

		memo[i][j][k] = res
		return res
	}

	return dfs(0, 0, 2)
}