func findEvenNumbers(digits []int) []int {
	out := make([]int, 0)
	cnt := make([]int, 10)

	for _, d := range digits {
		cnt[d]++
	}

	for d1 := 1; d1 < 10; d1++ {
		if cnt[d1] == 0 {
			continue
		}
		cnt[d1]--
		for d2 := range 10 {
			if cnt[d2] == 0 {
				continue
			}
			cnt[d2]--
			for d3 := 0; d3 < 10; d3 += 2 {
				if cnt[d3] == 0 {
					continue
				}
				out = append(out, d1*100+d2*10+d3)
			}
			cnt[d2]++
		}
		cnt[d1]++
	}

	return out
}
