import (
	"slices"
)

func sortMatrix(grid [][]int) [][]int {
	n := len(grid)
	buf := make([]int, 0, n)

	var sorter func([][]int, []int, int, int, bool)
	sorter = func(mat [][]int, b []int, r, c int, rev bool) {
		if r >= len(mat) || c >= len(mat) {
			if rev {
				slices.SortFunc(b, func(a, b int) int {
					return b - a
				})
			} else {
				slices.SortFunc(b, func(a, b int) int {
					return a - b
				})
			}
			return
		}

		b = append(b, mat[r][c])
		sorter(mat, b, r+1, c+1, rev)
		grid[r][c] = b[len(b)-1]
	}

	for i := range n {
		sorter(grid, buf, i, 0, true)
	}

	for j := 1; j < n; j++ {
		sorter(grid, buf, 0, j, false)
	}

	return grid
}
