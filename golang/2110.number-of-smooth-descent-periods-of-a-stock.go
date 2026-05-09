
func getDescentPeriods(prices []int) int64 {
	prev := -1
	window := 1
	total := 0

	for _, price := range prices {
		if prev-1 == price {
			window++
		} else {
			window = 1
		}

		total += window
		prev = price
	}

	return int64(total)
}
