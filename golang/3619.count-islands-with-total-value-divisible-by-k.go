func dfsGrid(grid [][]int, r, c int) int {
	if r < 0 || c < 0 || r >= len(grid) || c >= len(grid[0]) || grid[r][c] == 0 {
		return 0
	}

	res := grid[r][c]
	grid[r][c] = 0

	res += dfsGrid(grid, r+1, c)
	res += dfsGrid(grid, r, c+1)
	res += dfsGrid(grid, r-1, c)
	res += dfsGrid(grid, r, c-1)

	return res
}

func countIslands(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])
	count := 0

	for r := range m {
		for c := range n {
			if grid[r][c] == 0 {
				continue
			}

			if dfsGrid(grid, r, c)%k == 0 {
				count++
			}
		}
	}

	return count
}