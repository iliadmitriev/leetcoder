func minimumTotal(triangle [][]int) int {
	for i := len(triangle) - 2; i >= 0; i-- {
		for j := range len(triangle[i]) {
			triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
		}
	}

	return triangle[0][0]
}
