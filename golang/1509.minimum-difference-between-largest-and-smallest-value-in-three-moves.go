func minDifference(nums []int) int {
	n := len(nums)
	if n < 5 {
		return 0
	}

	sort.Ints(nums)

	ans := nums[n-4] - nums[0]
	for k := 0; k < 4; k++ {
		ans = min(ans, nums[n-4+k]-nums[k])
	}

	return ans
}
