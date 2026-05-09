func setZeroes(matrix [][]int) {
	m, n := len(matrix), len(matrix[0])
	row, col := make([]bool, m), make([]bool, n)

	for i := range m {
		for j := range n {
			if matrix[i][j] == 0 {
				row[i], col[j] = true, true
			}
		}
	}

	for i := range m {
		if !row[i] {
			continue
		}

		for j := range n {
			matrix[i][j] = 0
		}
	}

	for i := range n {
		if !col[i] {
			continue
		}

		for j := range m {
			matrix[j][i] = 0
		}
	}
}
