func numberOfAlternatingGroups(colors []int) int {
	count := 0

	n := len(colors)

	for i := 0; i < n; i++ {
		if colors[i] != colors[(n+i-1)%n] && colors[i] != colors[(i+1)%n] {
			count++
		}
	}

	return count
}
