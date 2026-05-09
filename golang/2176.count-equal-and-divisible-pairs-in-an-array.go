func countPairs(nums []int, k int) int {
	pairs := 0

	cache := make(map[int][]int)
	for i, num := range nums {
		cache[num] = append(cache[num], i)
	}

	for _, idxs := range cache {
		if len(idxs) < 2 {
			continue
		}

		gcds := make(map[int]int)

		for _, idx := range idxs {
			gcdI := getGCD(idx, k)

			for gcdJ, cnt := range gcds {
				if gcdI*gcdJ%k == 0 {
					pairs += cnt
				}
			}

			gcds[gcdI]++
		}
	}

	return pairs
}

func getGCD(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}
