var direct = [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

func dfsCheck(grid [][]int, r, c, maxGold int, visited [][]bool) int {
	if r < 0 || c < 0 || r >= len(grid) || c >= len(grid[0]) || visited[r][c] || grid[r][c] == 0 {
		return 0
	}

	res := 0
	visited[r][c] = true

	for _, dir := range direct {
		res = max(res, dfsCheck(grid, r+dir[0], c+dir[1], maxGold, visited))
	}

	visited[r][c] = false

	return res + grid[r][c]
}

func getMaximumGold(grid [][]int) int {
	ROWS, COLS := len(grid), len(grid[0])

	visited := make([][]bool, ROWS)
	for r := 0; r < ROWS; r++ {
		visited[r] = make([]bool, COLS)
	}

	maxGold := 0

	for r := 0; r < ROWS; r++ {
		for c := 0; c < COLS; c++ {
			if visited[r][c] || grid[r][c] == 0 {
				continue
			}

			maxGold = max(maxGold, dfsCheck(grid, r, c, maxGold, visited))

		}
	}

	return maxGold
}
