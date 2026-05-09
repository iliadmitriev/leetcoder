func numRabbits(answers []int) int {
	m := make(map[int]int)
	total := 0

	for _, v := range answers {
		m[v]++
	}

	for k, v := range m {
		total += (k + v) / (k + 1) * (k + 1)
	}

	return total
}
