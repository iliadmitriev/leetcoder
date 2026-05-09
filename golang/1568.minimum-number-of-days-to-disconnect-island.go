
var (
	time int      = 0
	DIRS [][2]int = [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
)

func minDays(grid [][]int) int {
	time = 0

	m, n := len(grid), len(grid[0])
	disc, low := make([][]int, m), make([][]int, m)
	for i := 0; i < m; i++ {
		disc[i], low[i] = make([]int, n), make([]int, n)
		for j := 0; j < n; j++ {
			disc[i][j], low[i][j] = -1, -1
		}
	}

	hasArticularPoints := false
	land, island := 0, 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 {
				continue
			}

			land++

			if disc[i][j] == -1 {
				island++
				hasArticularPoints = hasArticularPointsDFS(grid, disc, low, i, j, [2]int{-1, -1}) ||
					hasArticularPoints
			}
		}
	}

	if island != 1 {
		return 0
	} else if land == 1 || hasArticularPoints {
		return 1
	}

	return 2
}

func isValidLand(grid [][]int, r, c int) bool {
	return r >= 0 && c >= 0 && r < len(grid) && c < len(grid[0]) && grid[r][c] == 1
}

func hasArticularPointsDFS(grid, disc, low [][]int, r, c int, parent [2]int) bool {
	hasArticularPoints := false
	disc[r][c], low[r][c] = time, time
	children := 0
	time++

	for _, dir := range DIRS {
		nr := r + dir[0]
		nc := c + dir[1]

		if !isValidLand(grid, nr, nc) {
			continue
		}

		if disc[nr][nc] == -1 {
			children++

			hasArticularPoints = hasArticularPointsDFS(grid, disc, low, nr, nc, [2]int{r, c}) ||
				hasArticularPoints

			low[r][c] = min(low[r][c], low[nr][nc])

			if parent[0] != -1 && parent[1] != -1 && low[nr][nc] >= disc[r][c] {
				hasArticularPoints = true
			}

		} else if parent[0] != nr || parent[1] != nc {
			low[r][c] = min(low[r][c], disc[nr][nc])
		}
	}

	if parent[0] == -1 && parent[1] == -1 && children > 1 {
		hasArticularPoints = true
	}

	return hasArticularPoints
}
