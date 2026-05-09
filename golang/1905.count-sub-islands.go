func countSubIslands(grid1 [][]int, grid2 [][]int) int {
	M, N := len(grid1), len(grid1[0])

	visited := make([][]bool, M)
	for i := 0; i < M; i++ {
		visited[i] = make([]bool, N)
	}

	counter := 0

	for r := 0; r < M; r++ {
		for c := 0; c < N; c++ {
			if !visited[r][c] && grid2[r][c] == 1 {
				counter += __dfsCountSubIslands(r, c, grid1, grid2, visited)
			}
		}
	}

	return counter
}

func __dfsCountSubIslands(row, col int, grid1, grid2 [][]int, visited [][]bool) int {
	M, N := len(grid1), len(grid1[0])

	visited[row][col] = true
	isSubIsland := grid1[row][col]

	for _, d := range [][2]int{[2]int{1, 0}, [2]int{0, 1}, [2]int{-1, 0}, [2]int{0, -1}} {
		nr, nc := row+d[0], col+d[1]

		if 0 <= nr && nr < M && 0 <= nc && nc < N && !visited[nr][nc] && grid2[nr][nc] == 1 {
			isSubIsland *= __dfsCountSubIslands(nr, nc, grid1, grid2, visited)
		}
	}

	return isSubIsland
}
