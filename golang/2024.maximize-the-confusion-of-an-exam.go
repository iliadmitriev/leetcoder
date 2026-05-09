func maxConsecutiveAnswers(answerKey string, k int) int {
	maxConsecutive := 0
	lT, lF := 0, 0
	kT, kF := k, k

	for r := range answerKey {
		if answerKey[r] == 'T' {
			kF--
		} else {
			kT--
		}

		if kT < 0 {
			if answerKey[lT] == 'F' {
				kT++
			}
			lT++
		}

		if kF < 0 {
			if answerKey[lF] == 'T' {
				kF++
			}
			lF++
		}

		maxConsecutive = max(maxConsecutive, max(r-lT, r-lF)+1)
	}

	return maxConsecutive
}
