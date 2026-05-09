func minimumArea(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	left, right, top, bottom := n, -1, m, -1

	for i := range m {
		for j := range n {
			if grid[i][j] == 1 {
				left = min(left, j)
				right = max(right, j)
				top = min(top, i)
				bottom = max(bottom, i)
			}
		}
	}

	return max(right-left+1, 0) * max(bottom-top+1, 0)
}
