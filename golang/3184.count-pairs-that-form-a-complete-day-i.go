func countCompleteDayPairs(hours []int) int {
	count := make([]int, 24)
	for _, h := range hours {
		count[h%24]++
	}

	h0 := combinationsWithoutRep(count[0], 2)
	h12 := combinationsWithoutRep(count[12], 2)
	other := 0

	for i := 1; i < 12; i++ {
		other += count[i] * count[24-i]
	}

	return h0 + h12 + other
}

func combinationsWithoutRep(n, k int) int {
	if k > n {
		return 0
	}

	if k > n/2 {
		k = n - k
	}

	ans := 1
	for i := 1; i <= k; i++ {
		ans *= n - k + i
		ans /= i
	}

	return ans
}
