func countSeniors(details []string) int {
	count := 0

	for i := range details {
		if details[i][11] > '6' || (details[i][11] > '5' && details[i][12] > '0') {
			count++
		}
	}

	return count
}
