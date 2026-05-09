func restoreMatrix(rowSum []int, colSum []int) [][]int {
	m, n := len(rowSum), len(colSum)

	mat := make([][]int, m)
	for i := range mat {
		mat[i] = make([]int, n)
	}

	// O(max(m, n))
	i, j := 0, 0
	for i < m && j < n {
		mat[i][j] = min(rowSum[i], colSum[j])
		rowSum[i] -= mat[i][j]
		colSum[j] -= mat[i][j]

		if rowSum[i] == 0 {
			i++
		}

		if colSum[j] == 0 {
			j++
		}
	}

	return mat
}
