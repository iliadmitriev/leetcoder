
func bestClosingTime(customers string) int {
	totalPenalty := strings.Count(customers, "Y")

	minPenalty := totalPenalty
	curPenalty := totalPenalty
	earliestHour := 0

	for i, b := range customers {
		if b == 'N' {
			curPenalty++
		} else {
			curPenalty--
		}

		if curPenalty < minPenalty {
			minPenalty = curPenalty
			earliestHour = i + 1
		}
	}

	return earliestHour
}
