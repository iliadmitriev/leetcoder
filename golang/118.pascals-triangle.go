func generate(numRows int) [][]int {
	pas := make([][]int, numRows)

	for i := range numRows {
		pas[i] = make([]int, i+1)
		pas[i][0] = 1
		pas[i][i] = 1

		for j := 1; j < i; j++ {
			pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
		}
	}

	return pas
}
