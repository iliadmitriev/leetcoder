func distinctDifferenceArray(nums []int) []int {
	prefixCount, suffixCount := 0, 0

	prefix := make([]int, 51)
	suffix := make([]int, 51)

	for _, num := range nums {
		suffix[num]++
		if suffix[num] == 1 {
			suffixCount++
		}
	}

	res := make([]int, 0, len(nums))
	for _, num := range nums {
		prefix[num]++
		if prefix[num] == 1 {
			prefixCount++
		}
		suffix[num]--
		if suffix[num] == 0 {
			suffixCount--
		}
		res = append(res, prefixCount-suffixCount)
	}

	return res
}
