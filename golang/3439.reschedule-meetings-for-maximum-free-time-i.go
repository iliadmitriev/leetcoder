func maxFreeTime(eventTime int, k int, startTime []int, endTime []int) int {
	n := len(startTime)
	freeTime, maxFreeTime := 0, 0
	spaces := make([]int, 0, n+1)

	prev := 0
	for i := range n {
		spaces = append(spaces, startTime[i]-prev)
		prev = endTime[i]
	}
	spaces = append(spaces, eventTime-prev)

	for right := range n + 1 {
		freeTime += spaces[right]
		if right-k-1 >= 0 {
			freeTime -= spaces[right-k-1]
		}

		maxFreeTime = max(maxFreeTime, freeTime)
	}

	return maxFreeTime
}
