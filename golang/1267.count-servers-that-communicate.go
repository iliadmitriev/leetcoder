func countServers(grid [][]int) int {
	NROWS, NCOLS := len(grid), len(grid[0])
	count := 0
	adjRow, adjCol := make([][]int, NROWS), make([][]int, NCOLS)
	servers := make([][2]int, 0)
	vis := make(map[[2]int]bool)

	for r := 0; r < NROWS; r++ {
		for c := 0; c < NCOLS; c++ {
			if grid[r][c] == 1 {
				adjRow[r] = append(adjRow[r], c)
				adjCol[c] = append(adjCol[c], r)
				servers = append(servers, [2]int{r, c})
			}
		}
	}

	for _, server := range servers {
		if vis[server] {
			continue
		}

		network := countServerBFS(server, vis, adjRow, adjCol)
		if network > 1 {
			count += network
		}

	}

	return count
}

func countServerBFS(start [2]int, vis map[[2]int]bool, adjRow, adjCol [][]int) int {
	count := 0
	q := [][2]int{start}
	vis[start] = true

	for len(q) > 0 {
		server := q[0]
		q = q[1:]
		row, col := server[0], server[1]
		count++

		for _, ncol := range adjRow[row] {
			if col != ncol && !vis[[2]int{row, ncol}] {
				q = append(q, [2]int{row, ncol})
				vis[[2]int{row, ncol}] = true
			}
		}

		for _, nrow := range adjCol[col] {
			if row != nrow && !vis[[2]int{nrow, col}] {
				q = append(q, [2]int{nrow, col})
				vis[[2]int{nrow, col}] = true
			}
		}
	}

	return count
}
