func absByteDiff(a, b byte) int {
	if a > b {
		return int(a - b)
	}
	return int(b - a)
}

func equalSubstring(s string, t string, maxCost int) int {
	maxSub := 0
	cost := 0
	n := len(s)

	for i, j := 0, 0; i < n; i++ {
		cost += absByteDiff(s[i], t[i])

		for cost > maxCost {
			cost -= absByteDiff(s[j], t[j])
			j++
		}

		if maxSub < i-j+1 {
			maxSub = i - j + 1
		}
	}

	return maxSub
}
