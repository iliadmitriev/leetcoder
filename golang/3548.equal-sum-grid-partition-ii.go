func canPartitionGrid(grid [][]int) bool {
	type point struct {
		r, c int
	}

	// canRemoves checks if point (i,j) can be removed within the bounds
	// without splitting rectangle in two disjoint sections
	// bounds:
	// r1,c1 top left
	// r2,c2 bottom left
	// point: i, j
	canRemove := func(r1, c1, r2, c2, i, j int) bool {
		rows := r2 - r1 + 1
		cols := c2 - c1 + 1

		if rows*cols <= 1 {
			return false
		}

		if rows == 1 { // if it's an only row, then only left and right can be deleted
			return j == c1 || j == c2
		}

		if cols == 1 { // if it's an only colum, then only top and bottom can be deleted
			return i == r1 || i == r2
		}

		return true
	}

	m, n := len(grid), len(grid[0])

	cache := make(map[int][]point, m*n)
	row := make([]int, m)
	col := make([]int, n)

	top, bottom := 0, 0
	left, right := 0, 0
	all := 0

	for i := range m {
		for j := range n {
			all += grid[i][j]
			cache[grid[i][j]] = append(cache[grid[i][j]], point{i, j})
			row[i] += grid[i][j]
			col[j] += grid[i][j]
		}
	}

	for i := range m - 1 {
		top += row[i]

		bottom = all - top
		if top == bottom {
			return true
		}

		// try to find and remove diff
		diff := max(top-bottom, bottom-top)
		for _, p := range cache[diff] {
			if top > bottom {
				if p.r <= i && canRemove(0, 0, i, n-1, p.r, p.c) {
					return true
				}
			} else {
				if p.r > i && canRemove(i+1, 0, m-1, n-1, p.r, p.c) {
					return true
				}
			}
		}

	}

	for j := range n - 1 {
		left += col[j]

		right = all - left
		if left == right {
			return true
		}

		// try to find and remove diff horizontal wise
		diff := max(left-right, right-left)
		for _, p := range cache[diff] {
			if left > right {
				if p.c <= j && canRemove(0, 0, m-1, j, p.r, p.c) {
					return true
				}
			} else {
				if p.c > j && canRemove(0, j+1, m-1, n-1, p.r, p.c) {
					return true
				}
			}
		}
	}

	return false
}