func maxEqualRowsAfterFlips(matrix [][]int) int {
	m, n := len(matrix), len(matrix[0])
	count := make(map[string]int, m)

	for i := 0; i < m; i++ {
		var row bytes.Buffer
		for j := 0; j < n; j++ {
			if matrix[i][j] == matrix[i][0] {
				row.WriteByte('1')
			} else {
				row.WriteByte('0')
			}
		}

		count[row.String()]++
	}

	maxCount := 0
	for _, v := range count {
		if v > maxCount {
			maxCount = v
		}
	}

	return maxCount
}
