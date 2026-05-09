func maxScore(s string) int {
	maxScore := 0
	score := 0
	bt := []byte(s)

	for _, ch := range bt {
		if ch == '1' {
			score++
		}
	}

	for i := 0; i < len(bt)-1; i++ {
		if bt[i] == '0' {
			score++
		} else {
			score--
		}

		maxScore = max(maxScore, score)
	}

	return maxScore
}
