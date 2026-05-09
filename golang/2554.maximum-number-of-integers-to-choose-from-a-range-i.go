func maxCount(banned []int, n int, maxSum int) int {
	maxBanned := n
	for _, b := range banned {
		if maxBanned < b {
			maxBanned = b
		}
	}

	bannedSet := make([]bool, maxBanned+1)
	for _, b := range banned {
		bannedSet[b] = true
	}

	total, count := 0, 0

	for i := 1; i <= n && i+total <= maxSum; i++ {
		if bannedSet[i] {
			continue
		}

		total += i
		count++
	}

	return count
}
