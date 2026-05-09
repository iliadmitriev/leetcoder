func reverseSubmatrix(grid [][]int, x int, y int, k int) [][]int {
	if k == 1 {
		return grid
	}

	for i := 0; i < k/2; i++ { // delta x (row)
		for j := 0; j < k; j++ { // delta y (column)
			grid[x+i][y+j], grid[x+k-1-i][y+j] = grid[x+k-1-i][y+j], grid[x+i][y+j]
		}
	}

	return grid
}