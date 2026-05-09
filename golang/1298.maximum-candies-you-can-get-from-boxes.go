func maxCandies(status []int, candies []int, keys [][]int, containedBoxes [][]int, initialBoxes []int) int {
	total := 0
	q := make([]int, 0, len(status))

	// statuses:
	// 0: locked, not visited
	// 1: unlocked, not visited
	// -1: locked, visited
	// -2: unlocked, visited

	for _, i := range initialBoxes {
		switch status[i] {
		case 1:
			q = append(q, i)
			status[i] = -2
		case 0:
			status[i] = -1
		}
	}

	for len(q) > 0 {
		box := q[0]
		q = q[1:]
		total += candies[box]

		for _, key := range keys[box] {
			if status[key] == -1 { // if it was visited but locked
				q = append(q, key) // visit it again
			}
			status[key] = 1
		}

		for _, contained := range containedBoxes[box] {
			switch status[contained] {
			case 1:
				q = append(q, contained)
				status[contained] = -2
			case 0:
				status[contained] = -1
			}
		}

	}

	return total
}
