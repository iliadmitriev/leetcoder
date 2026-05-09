func maxSideLength(mat [][]int, threshold int) int {
	m, n := len(mat), len(mat[0])
	k := min(m, n)

	pre := make([][]int, m+1)
	pre[0] = make([]int, n+1)

  // pre-calculate prefix matrix
  // O(m*n)
	for i := 1; i < 1+m; i++ {
		pre[i] = make([]int, n+1)

		for j := 1; j < 1+n; j++ {
			pre[i][j] = pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + mat[i-1][j-1]
		}
	}

  // O(1)
	area := func(i, j, sz int) int {
		return pre[i+sz][j+sz] - pre[i][j+sz] - pre[i+sz][j] + pre[i][j]
	}

  // check if square with side of length sz is found
  // O(m*n)
	check := func(sz int) bool {
		for i := range m - sz + 1 {
			for j := range n - sz + 1 {
				if area(i, j, sz) <= threshold {
					return true
				}
			}
		}

		return false
	}

	lo, hi := 0, k+1
	res := 0

	for lo < hi {
		mid := (lo + hi) / 2

		if check(mid) {
			lo = mid + 1
			res = mid
		} else {
			hi = mid
		}
	}

	return res
}