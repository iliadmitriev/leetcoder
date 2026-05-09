func busyStudent(startTime []int, endTime []int, queryTime int) int {
	n := len(startTime)
	count := 0

	for i := 0; i < n; i++ {
		if startTime[i] <= queryTime && queryTime <= endTime[i] {
			count++
		}
	}

	return count
}
