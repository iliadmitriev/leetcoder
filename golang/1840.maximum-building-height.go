func maxBuilding(n int, restrictions [][]int) int {

	topHeight := 0
	r := make([][]int, 0, len(restrictions)+2)
	r = append(r, []int{1, 0})
	r = append(r, restrictions...)

  slices.SortFunc(r, func(a, b []int) int {
    return a[0] - b[0]
  })

	// if last building is not restricted
	// add sentinel, maximum possible value
	if r[len(r)-1][0] < n {
		r = append(r, []int{n, n - 1})
	}

	// slope eq: dy = m * dx
	// A left: y1 - y = 1 * (x1 - x)
	// B right: y2 - y = -1 * (x2 - x)
	// A + B:
	// y1 + y2 - y - y = x1 - x - x2 + x
	// y = (y1 + y2 - x1 + x2) / 2
	solve := func(x1, y1, x2, y2 int) int {
		return (y1 + y2 - x1 + x2) / 2
	}

	// height limit between two restrictions:
	// dy <= dx
	// abs(y2 - y1) <= abs(x2 - x1)
	// y2 - y1 <= abs(x2 - x1)
	// y2 <= y1 + abs(x2 - x1)
	cap := func(x1, y1, x2, y2 int) int {
		dx := x2 - x1
		if dx < 0 {
			dx = -dx
		}

		return min(y2, y1+dx)
	}

	k := len(r)

	for i := 1; i < k; i++ {
		r[i][1] = cap(r[i-1][0], r[i-1][1], r[i][0], r[i][1])
	}

	for i := k - 2; i >= 0; i-- {
		r[i][1] = cap(r[i+1][0], r[i+1][1], r[i][0], r[i][1])
	}

	for i := 1; i < k; i++ {
		topHeight = max(
			topHeight,
			solve(r[i-1][0], r[i-1][1], r[i][0], r[i][1]),
		)
	}

	return topHeight
}