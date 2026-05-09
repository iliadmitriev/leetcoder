func missingRolls(rolls []int, mean int, n int) []int {
	m := len(rolls)
	total := (n + m) * mean

	for _, roll := range rolls {
		total -= roll
	}

	if (total < n) || (total > n*6) {
		return []int{}
	}

	res := make([]int, n)
	for i := 0; i < n; i++ {
		res[i] = total / n
	}

	for i := 0; i < total%n; i++ {
		res[i]++
	}

	return res
}
