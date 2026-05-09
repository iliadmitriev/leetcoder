func numMagicSquaresInside(grid [][]int) int {
	count := 0

	m, n := len(grid), len(grid[0])
	for i := 0; i < m-2; i++ {
		for j := 0; j < n-2; j++ {
			if isMagicSquare(grid, i, j) {
				count++
			}
		}
	}

	return count
}

func isMagicSquare(grid [][]int, y, x int) bool {
	target := 15
	N := 3
	s := make([]int, 10)
	for dy := 0; dy < N; dy++ {
		for dx := 0; dx < N; dx++ {
			v := grid[y+dy][x+dx]
			if v > 9 || v < 1 {
				return false
			}
			s[v] = 1
		}
	}

	for i := 1; i < 10; i++ {
		if s[i] != 1 {
			return false
		}
	}

	diag1, diag2 := 0, 0
	for d := 0; d < N; d++ {
		diag1 += grid[y+d][x+d]
		diag2 += grid[y+d][x+N-1-d]
	}

	if diag1 != target || diag2 != target {
		return false
	}

	for d1 := 0; d1 < N; d1++ {
		rowSum, colSum := 0, 0
		for d2 := 0; d2 < N; d2++ {
			rowSum += grid[y+d1][x+d2]
			colSum += grid[y+d2][x+d1]
		}

		if rowSum != target || colSum != target {
			return false
		}
	}

	return true
}