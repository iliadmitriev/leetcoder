func numEquivDominoPairs(dominoes [][]int) int {
	total := 0
	cache := [10][10]int{}

	for _, domino := range dominoes {
		a, b := domino[0], domino[1]

		if a > b {
			a, b = b, a
		}

		total += cache[a][b]
		cache[a][b]++
	}

	return total
}
