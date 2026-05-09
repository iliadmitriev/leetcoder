func dfsIslandCover(grid [][]byte, i, j int) {
	m, n := len(grid), len(grid[0])
	q := make([][2]int, 0)
	q = append(q, [2]int{i, j})
	grid[i][j] = 1

	for len(q) > 0 {
		y, x := q[0][0], q[0][1]
		q = q[1:]

		for _, d := range [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}} {
			ny, nx := y+d[0], x+d[1]
			if 0 <= ny && ny < m && 0 <= nx && nx < n && grid[ny][nx] == 0 {
				grid[ny][nx] = 1
				q = append(q, [2]int{ny, nx})
			}
		}
	}
}

func regionsBySlashes(grid []string) int {
	m, n := len(grid), len(grid[0])
	islands := 0

	upscale := make([][]byte, m*3)
	for i := 0; i < m*3; i++ {
		upscale[i] = make([]byte, n*3)
	}

	// fill upscaled matrix
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == '\\' {
				for k := 0; k < 3; k++ {
					upscale[i*3+k][j*3+k] = 1
				}
			} else if grid[i][j] == '/' {
				for k := 0; k < 3; k++ {
					upscale[i*3+k][j*3+2-k] = 1
				}
			}
		}
	}
	// bfs from each cell
	for i := 0; i < m*3; i++ {
		for j := 0; j < n*3; j++ {
			if upscale[i][j] == 0 {
				islands++
				dfsIslandCover(upscale, i, j)
			}
		}
	}

	return islands
}
