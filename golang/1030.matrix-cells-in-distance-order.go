func allCellsDistOrder(rows int, cols int, rCenter int, cCenter int) [][]int {
	res := make([][]int, 0, rows*cols)

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			res = append(res, []int{i, j})
		}
	}

	sort.Slice(res, func(i, j int) bool {
		return abs(res[i][0]-rCenter)+abs(res[i][1]-cCenter) < abs(res[j][0]-rCenter)+abs(res[j][1]-cCenter)
	})

	return res
}
