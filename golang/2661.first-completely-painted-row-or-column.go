func firstCompleteIndex(arr []int, mat [][]int) int {
	NROWS, NCOLS := len(mat), len(mat[0])
	rows, cols := make([]int, NROWS*NCOLS+1), make([]int, NROWS*NCOLS+1)
	rowCount, colCount := make([]int, NROWS), make([]int, NCOLS)

	for i := 0; i < NROWS; i++ {
		for j := 0; j < NCOLS; j++ {
			rows[mat[i][j]] = i
			cols[mat[i][j]] = j
			rowCount[i]++
			colCount[j]++
		}
	}

	for idx := range arr {
		row, col := rows[arr[idx]], cols[arr[idx]]
		rowCount[row]--
		colCount[col]--

		if rowCount[row] == 0 || colCount[col] == 0 {
			return idx
		}
	}

	return -1
}
