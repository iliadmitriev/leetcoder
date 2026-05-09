func numberOfAlternatingGroups(colors []int, k int) int {
	n := len(colors)
	curAlt, alt := 1, 0

	for i := 1; i < n+k-1; i++ {
		if colors[(i-1)%n] == colors[i%n] {
			curAlt = 1
			continue
		}

		curAlt++
		if curAlt >= k {
			alt++
		}
	}

	return alt
}
