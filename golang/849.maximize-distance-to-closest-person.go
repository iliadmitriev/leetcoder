func maxDistToClosest(seats []int) int {
	maxDist := 0
	prev := -1

	for i, p := range seats {
		if p == 0 {
			continue
		}

		if prev == -1 {
			maxDist = max(maxDist, (i-prev)-1)
		} else {
			maxDist = max(maxDist, (i-prev)/2)
		}

		prev = i
	}

	maxDist = max(maxDist, len(seats)-prev-1)

	return maxDist
}