type interval struct {
	l, r int
}

func checkValidRangeCuts(intervals []interval) bool {
	count, right := 0, 0

	slices.SortFunc(intervals, func(a, b interval) int {
		return a.l - b.l
	})

	for _, i := range intervals {
		if i.l >= right {
			count++
		}

		right = max(right, i.r)
		if count == 3 {
			return true
		}

	}

	return count >= 3
}

func checkValidCuts(n int, rectangles [][]int) bool {
	m := len(rectangles)
	X, Y := make([]interval, 0, m), make([]interval, 0, m)
	for _, rect := range rectangles {
		X = append(X, interval{rect[0], rect[2]})
		Y = append(Y, interval{rect[1], rect[3]})
	}

	return checkValidRangeCuts(X) || checkValidRangeCuts(Y)
}
