
func countTotalScore(grid [][]int) int {
	score := 0
	lenRow, lenCol := len(grid), len(grid[0])
	for i := 0; i < lenRow; i++ {
		for j := 0; j < lenCol; j++ {
			score += grid[i][j] << (lenCol - j - 1)
		}
	}

	return score
}

func flipRow(grid [][]int, row int) {
	lenRow := len(grid[row])

	for j := 0; j < lenRow; j++ {
		grid[row][j] ^= 1
	}
}

func flipCol(grid [][]int, col int) {
	lenCol := len(grid)

	for i := 0; i < lenCol; i++ {
		grid[i][col] ^= 1
	}
}

func matrixScore(grid [][]int) int {
	lenRow, lenCol := len(grid), len(grid[0])

	for i := 0; i < lenRow; i++ {
		if grid[i][0] == 0 {
			flipRow(grid, i)
		}
	}

	for j := 0; j < lenCol; j++ {
		onesCount := 0
		for i := 0; i < lenRow; i++ {
			onesCount += grid[i][j]
		}

		if 2*onesCount < lenRow {
			flipCol(grid, j)
		}
	}

	return countTotalScore(grid)
}
