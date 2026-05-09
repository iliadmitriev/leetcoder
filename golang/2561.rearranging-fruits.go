func minCost(basket1 []int, basket2 []int) int64 {
	swap := make([]int, 0)
	freq := make(map[int]int, len(basket1))
	minFruit := basket1[0]

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	// balance fruits
	for _, fruit := range basket1 {
		freq[fruit]++
		minFruit = min(minFruit, fruit)
	}

	for _, fruit := range basket2 {
		freq[fruit]--
		minFruit = min(minFruit, fruit)
	}

	for fruit, cnt := range freq {
		if cnt%2 != 0 {
			return -1
		}

		imbalance := abs(cnt) / 2
		for range imbalance {
			swap = append(swap, fruit)
		}
	}

	if len(swap) == 0 {
		return 0
	}

	sort.Ints(swap)

	cost := 0

	for i := range len(swap) / 2 {
		cost += min(2*minFruit, swap[i])
	}

	return int64(cost)
}
