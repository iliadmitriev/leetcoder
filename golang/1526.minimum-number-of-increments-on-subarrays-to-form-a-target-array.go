func minNumberOperations(target []int) int {
	total := 0
	prev := 0

	for _, num := range target {
		if num > prev {
			total += num - prev
		}

		prev = num
	}

	return total
}
