func maxFreqSum(s string) int {
	const (
		ALPHABET = 26
		BASE     = 'a'
	)

	var (
		cnt                    [ALPHABET]int
		maxVowel, maxConsonant int
	)

	for _, ch := range s {
		cnt[ch-BASE]++
	}

	for i, ch := range cnt {
		if i == 0 || i == 4 || i == 8 || i == 14 || i == 20 {
			maxVowel = max(maxVowel, ch)
		} else {
			maxConsonant = max(maxConsonant, ch)
		}
	}

	return maxVowel + maxConsonant
}
