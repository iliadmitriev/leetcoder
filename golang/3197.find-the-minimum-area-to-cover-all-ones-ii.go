
func minimumSum(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	ms := minSquareCounter{m: make(map[[4]int]int)}
	total := m * n

	// horizontal split in three non-empty parts (top, middle, bottom)
	for r1 := 1; r1 < m-1; r1++ {
		for r2 := r1 + 1; r2 < m; r2++ {
			total = min(total,
				ms.minSquare(grid, 0, 0, r1, n)+
					ms.minSquare(grid, r1, 0, r2, n)+
					ms.minSquare(grid, r2, 0, m, n),
			)
		}
	}

	// vertical split in three non-empty parts (left, middle, right)
	for c1 := 1; c1 < n-1; c1++ {
		for c2 := c1 + 1; c2 < n; c2++ {
			total = min(total,
				ms.minSquare(grid, 0, 0, m, c1)+
					ms.minSquare(grid, 0, c1, m, c2)+
					ms.minSquare(grid, 0, c2, m, n),
			)
		}
	}

	// horizontal and then vertical
	// vertical and then horizontal
	for r := 1; r < m; r++ {
		for c := 1; c < n; c++ {
			// horizontal and then vertical (top, bottom left, bottom right)
			total = min(total,
				ms.minSquare(grid, 0, 0, r, n)+
					ms.minSquare(grid, r, 0, m, c)+
					ms.minSquare(grid, r, c, m, n),
			)
			// horizontal and then vertical (bottom, top left, top right)
			total = min(total,
				ms.minSquare(grid, r, 0, m, n)+
					ms.minSquare(grid, 0, 0, r, c)+
					ms.minSquare(grid, 0, c, r, n),
			)
			// vertical and then horizontal (left, top right, bottom right)
			total = min(total,
				ms.minSquare(grid, 0, 0, m, c)+
					ms.minSquare(grid, 0, c, r, n)+
					ms.minSquare(grid, r, c, m, n),
			)
			// vertical and then horizontal (right, top left, bottom left)
			total = min(total,
				ms.minSquare(grid, 0, c, m, n)+
					ms.minSquare(grid, 0, 0, r, c)+
					ms.minSquare(grid, r, 0, m, c),
			)
		}
	}

	return total
}

type minSquareCounter struct {
	m map[[4]int]int
}

// minSquare get square of the minimum rectangle area that contains all 1s
// of the part of the grid from (r1, c1) inclusive to (r2, c2) exclusive.
func (m *minSquareCounter) minSquare(grid [][]int, r1, c1, r2, c2 int) int {
	if res, ok := m.m[[4]int{r1, c1, r2, c2}]; ok {
		return res
	}

	left, right, top, bottom := c2, c1, r2, r1

	for i := r1; i < r2; i++ {
		for j := c1; j < c2; j++ {
			if grid[i][j] == 1 {
				left = min(left, j)
				right = max(right, j)
				top = min(top, i)
				bottom = max(bottom, i)
			}
		}
	}

	height, width := bottom-top+1, right-left+1

	if height > 0 && width > 0 {
		res := height * width
		m.m[[4]int{r1, c1, r2, c2}] = res
		return res
	}

	return 0
}
