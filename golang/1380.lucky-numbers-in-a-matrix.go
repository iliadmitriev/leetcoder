func luckyNumbers(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])

	minRow := make([]int, m)
	maxCol := make([]int, n)

	for i := 0; i < m; i++ {
		minRow[i] = matrix[i][0]
		for j := 0; j < n; j++ {
			minRow[i] = min(matrix[i][j], minRow[i])
			maxCol[j] = max(matrix[i][j], maxCol[j])
		}
	}

	sort.Ints(minRow)
	sort.Ints(maxCol)
	res := make([]int, 0)

	for i, j := 0, 0; i < m && j < n; {
		if minRow[i] > maxCol[j] {
			j++
		} else if minRow[i] < maxCol[j] {
			i++
		} else {
			res = append(res, minRow[i])
			i++
			j++
		}
	}

	return res
}
