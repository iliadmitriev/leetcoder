func areaOfMaxDiagonal(dimensions [][]int) int {
	maxArea, maxDiagonal := 0, 0

	for _, dim := range dimensions {
		a, b := dim[0], dim[1]
		diagonal := a*a + b*b

		if diagonal > maxDiagonal {
			maxDiagonal = diagonal
			maxArea = a * b
		} else if diagonal == maxDiagonal {
			maxArea = max(maxArea, a*b)
		}
	}

	return maxArea
}
