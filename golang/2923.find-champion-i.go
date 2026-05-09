func findChampion(grid [][]int) int {
	n := len(grid)

	for i := 0; i < n; i++ {
		counter := 0

		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				counter++
			}
		}

		if counter == n-1 {
			return i
		}
	}

	return -1
}
