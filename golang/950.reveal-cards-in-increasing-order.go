func deckRevealedIncreasing(deck []int) []int {
	n := len(deck)

	sort.Ints(deck)
	res := make([]int, n)

	q := make([]int, 0, 2*n-1)

	for i := range deck {
		q = append(q, i)
	}

	for _, d := range deck {
		res[q[0]] = d
		q = q[1:]

		if len(q) > 0 {
			q = append(q, q[0])
			q = q[1:]
		}
	}

	return res
}
