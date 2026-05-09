func canPartitionGrid(grid [][]int) bool {

	var (
		all       int
		top, left int
		target    int
	)

	m, n := len(grid), len(grid[0])
	row := make([]int, m)
	col := make([]int, n)

	for i := range m {
		for j := range n {
			all += grid[i][j]
			row[i] += grid[i][j]
			col[j] += grid[i][j]
		}
	}

	// heuristic, if it's odd then it's impossible to split it in two equal parts
	if all%2 == 1 {
		return false
	}

	target = all / 2

	for i := range m - 1 {
		top += row[i]

		if top == target {
			return true
		}

		if top > target { // break early on target exceeding
			break
		}
	}

	for j := range n - 1 {
		left += col[j]

		if left == target {
			return true
		}

		if left > target { // break early on target exceeding
			break
		}
	}

	return false
}