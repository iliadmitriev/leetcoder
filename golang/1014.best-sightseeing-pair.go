func maxScoreSightseeingPair(values []int) int {
	maxScore, curScore := -values[0], 0

	for i, value := range values {
		maxScore = max(maxScore, curScore+value-i)
		curScore = max(curScore, value+i)
	}

	return maxScore
}
