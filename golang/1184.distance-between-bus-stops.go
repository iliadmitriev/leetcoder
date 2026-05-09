func distanceBetweenBusStops(distance []int, start int, destination int) int {
	total, diff := 0, 0

	if start > destination {
		start, destination = destination, start
	}

	for i := 0; i < len(distance); i++ {
		total += distance[i]
	}

	for i := start; i < destination; i++ {
		diff += distance[i]
	}

	return min(total-diff, diff)
}
