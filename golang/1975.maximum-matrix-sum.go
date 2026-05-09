func maxMatrixSum(matrix [][]int) int64 {
	m, n := len(matrix), len(matrix[0])
	minAbs := matrix[0][0]
	if minAbs < 0 {
		minAbs = -minAbs
	}

	countNeg := 0
    countZero := 0
	total := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {

			absVal := matrix[i][j]
			if absVal < 0 {
				absVal = -absVal
				countNeg++
			}
            if absVal == 0 {
                countZero++
            }

			minAbs = min(minAbs, absVal)
			total += absVal
		}
	}

	if countZero > 0 || countNeg%2 == 0 {
		return int64(total)
	}

	return int64(total - 2*minAbs)
}