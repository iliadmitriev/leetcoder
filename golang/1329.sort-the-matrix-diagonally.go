func diagonalSort(mat [][]int) [][]int {
	m, n := len(mat), len(mat[0]) // rows, cols
	k := min(m, n)                // diagonal length
	buf := make([]int, k)         // maximum possible length

	bufSort := func(r, c int) {
		p := 0 // length of buffer
		for i, j := r, c; i < m && j < n; i, j = i+1, j+1 {
			buf[p] = mat[i][j]
			p++
		}

		sort.Ints(buf[:p]) // sort only first p items

		p = 0

		for i, j := r, c; i < m && j < n; i, j = i+1, j+1 {
			mat[i][j] = buf[p]
			p++
		}
	}

	for i := m - 1; i > 0; i-- {
		bufSort(i, 0)
	}

	for j := 0; j < n; j++ {
		bufSort(0, j)
	}

	return mat
}