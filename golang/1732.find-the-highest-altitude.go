func largestAltitude(gain []int) int {
	runningMax := 0
	runningTotal := 0

	for _, g := range gain {
		runningTotal += g
		runningMax = max(runningMax, runningTotal)
	}

	return runningMax
}