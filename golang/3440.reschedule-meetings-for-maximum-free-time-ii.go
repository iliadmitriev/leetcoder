func maxFreeTime(eventTime int, startTime []int, endTime []int) int {
	n := len(startTime)
	spaces := make([]int, n+1)
	prev := 0

	for i := range n {
		spaces[i] = startTime[i] - prev
		prev = endTime[i]
	}

	spaces[n] = eventTime - prev

	maxFree := 0

	// get indexes of 3 largest spaces
	// to use them as candidates for slots
	a, b, c := -1, -1, -1
	for i := range n + 1 {
		if a == -1 || spaces[i] > spaces[a] {
			a, b, c = i, a, b
		} else if b == -1 || spaces[i] > spaces[b] {
			b, c = i, b
		} else if c == -1 || spaces[i] > spaces[c] {
			c = i
		}
	}

	for i := range n {
		mid := endTime[i] - startTime[i]
		left, right := spaces[i], spaces[i+1]

		maxFree = max(maxFree, left+right)

		// if one of a,b or c is not used by left(i) and right(i+1) and has enough space
		// then we can use it to move current meeting
		if (i != a && i+1 != a && mid <= spaces[a]) ||
			(i != b && i+1 != b && mid <= spaces[b]) ||
			(i != c && i+1 != c && mid <= spaces[c]) {
			maxFree = max(maxFree, left+mid+right)
		}
	}

	return maxFree
}
