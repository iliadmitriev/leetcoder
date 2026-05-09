func unequalTriplets(nums []int) int {
	freq := make(map[int]int)
	for _, v := range nums {
		freq[v]++
	}

	n := len(nums)
	totalCombs := countComb(n, 3)

	for _, v := range freq {
		if v == 1 {
			continue
		}

		three := countComb(v, 3)
		two := countComb(v, 2) * (n - v)
		totalCombs -= two + three
	}

	return totalCombs
}

func countComb(n, k int) int {
	if n < k {
		return 0
	}

	if n < 2*k {
		k = n - k
	}

	res := 1
	for d := 1; d <= k; d++ {
		res *= n
		res /= d
		n--
	}

	return res
}
