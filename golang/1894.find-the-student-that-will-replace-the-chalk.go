func chalkReplacer(chalk []int, k int) int {
	totalDemand := 0
	for _, v := range chalk {
		if totalDemand > k {
			break
		}

		totalDemand += v
	}

	k %= totalDemand

	for i, v := range chalk {
		if k < v {
			return i
		}

		k -= v
	}

	return 0
}
