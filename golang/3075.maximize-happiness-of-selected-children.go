
func maximumHappinessSum(happiness []int, k int) int64 {
	total := 0
	n := len(happiness)

	sort.Ints(happiness)

	for i := range k {
		value := max(0, happiness[n-i-1]-i)

		if value == 0 {
			break
		}

		total += value
	}

	return int64(total)
}
