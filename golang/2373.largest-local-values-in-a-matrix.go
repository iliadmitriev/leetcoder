func max2d(grid [][]int, r, c, kerlnel int) int {
	res := 0

	for i := r; i < r+kerlnel; i++ {
		for j := c; j < c+kerlnel; j++ {
			res = max(res, grid[i][j])
		}
	}

	return res
}

func largestLocal(grid [][]int) [][]int {
	n := len(grid) - 2
	res := make([][]int, n)
	for r := range res {
		res[r] = make([]int, n)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			res[i][j] = max2d(grid, i, j, 3)
		}
	}

	return res
}
