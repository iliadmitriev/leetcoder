func averageWaitingTime(customers [][]int) float64 {
	idleAt, start, total := 0, 0, 0
	n := len(customers)

	for i := 0; i < n; i++ {
		start = max(idleAt, customers[i][0])
		total += start - customers[i][0]
		total += customers[i][1]
		idleAt = start + customers[i][1]
	}

	return float64(total) / float64(n)
}
