func sumCounts(nums []int) int {
	n := len(nums)
	res := 0

	for i := 0; i < n; i++ {
		distinct := make(map[int]bool, n-i)
		for j := i; j < n; j++ {
			distinct[nums[j]] = true
			res += len(distinct) * len(distinct)
		}
	}

	return res
}
