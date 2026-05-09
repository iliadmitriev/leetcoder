func largestMagicSquare(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	k := min(m, n)

	h := make([][]int, m)
	v := make([][]int, m+1)
	largest := 1

	for i := range m {
		h[i] = make([]int, n+1)
		for j := 1; j < n+1; j++ {
			h[i][j] = h[i][j-1] + grid[i][j-1]
		}
	}
	v[0] = make([]int, n)
	for i := 1; i < m+1; i++ {
		v[i] = make([]int, n)
		for j := range n {
			v[i][j] = v[i-1][j] + grid[i-1][j]
		}
	}

	//fmt.Println(h)
	//fmt.Println(v)

	// O(m + n) -> O(1)
	checkIsMagic := func(i, j, sz int) bool {

		// check first horizontal and first vertical
		fh := h[i][j+sz] - h[i][j]
		fv := v[i+sz][j] - v[i][j]

		// early return
		if fh != fv {
			return false
		}

		// check all horizontals with early return
		for di := range sz {
			if fh != h[i+di][j+sz]-h[i+di][j] {
				return false
			}
		}

		// check all verticals with early return
		for dj := range sz {
			if fh != v[i+sz][j+dj]-v[i][j+dj] {
				return false
			}
		}

    // check diagonals
    d1, d2 := 0, 0
    for d := range sz {
      d1 += grid[i + d][j + d]
      d2 += grid[i + sz - d - 1][j + d]
    }
    if d1 != fv || d2 != fv {
      return false
    }

		return true
	}

	// O(m * n * k)
	for i := range m {
		for j := range n {
			rest := min(m-i, n-j)

			for sz := largest + 1; sz <= k && sz <= rest; sz++ {
				if checkIsMagic(i, j, sz) {
					largest = max(largest, sz)
				}
			}
		}
	}

	return largest
}