func findPoisonedDuration(timeSeries []int, duration int) int {
	poisoned := 0
	prev := -1

	for _, tm := range timeSeries {
		if prev < 0 || tm >= prev+duration {
			poisoned += duration
		} else {
			poisoned += tm - prev
		}

		prev = tm
	}

	return poisoned
}
