
type neighborSum struct {
	M, N int
	Data map[int][2]int
	Grid [][]int
}

func Constructor(grid [][]int) neighborSum {
	M, N := len(grid), len(grid[0])
	data := make(map[int][2]int, M*N)
	for i, r := range grid {
		for j, v := range r {
			data[v] = [2]int{i, j}
		}
	}
	return neighborSum{M, N, data, grid}
}

func (this *neighborSum) nodeSum(row, col int, shift [][2]int) int {
	s := 0
	for _, d := range shift {
		i, j := row+d[0], col+d[1]
		if i < 0 || j < 0 || i >= this.M || j >= this.N {
			continue
		}
		s += this.Grid[i][j]
	}

	return s
}

func (this *neighborSum) AdjacentSum(value int) int {
	if _, ok := this.Data[value]; !ok {
		return 0
	}

	return this.nodeSum(
		this.Data[value][0],
		this.Data[value][1],
		[][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}},
	)
}

func (this *neighborSum) DiagonalSum(value int) int {
	if _, ok := this.Data[value]; !ok {
		return 0
	}

	return this.nodeSum(
		this.Data[value][0],
		this.Data[value][1],
		[][2]int{{-1, -1}, {-1, 1}, {1, -1}, {1, 1}},
	)
}

/**
 * Your neighborSum object will be instantiated and called as such:
 * obj := Constructor(grid);
 * param_1 := obj.AdjacentSum(value);
 * param_2 := obj.DiagonalSum(value);
 */