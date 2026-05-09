func maximizeSquareHoleArea(n int, m int, hBars []int, vBars []int) int {
	sort.Ints(hBars)
	sort.Ints(vBars)

	getRange := func(data []int) int {
		prev := -1
		curRange := 0
		maxRange := 1
		for _, v := range data {
			if prev+1 == v {
				curRange++
			} else {
				maxRange = max(maxRange, curRange)
				curRange = 1
			}
			prev = v
		}

		maxRange = max(maxRange, curRange)

		return maxRange + 1
	}

	width := getRange(vBars)
	height := getRange(hBars)

	side := min(height, width)

	fmt.Println(height, width, side)
	return side * side
}