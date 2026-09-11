func totalNumbers(digits []int) int {
	cnt := make([]uint8, 10)
	for _, n := range digits {
		cnt[n]++
	}

	total := 0

	for c := 1; c < 10; c++ {
		if cnt[c] == 0 {
			continue
		}

		cnt[c]--

		for d := 0; d < 10; d++ {
			if cnt[d] == 0 {
				continue
			}

			cnt[d]--
			for u := 0; u < 10; u += 2 {
				if cnt[u] == 0 {
					continue
				}

				total++
			}

			cnt[d]++
		}

		cnt[c]++
	}

	return total
}