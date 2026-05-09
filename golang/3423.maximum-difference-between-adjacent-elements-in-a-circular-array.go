func maxAdjacentDistance(nums []int) int {
	n := len(nums)
	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}

	maxAbs := abs(nums[0] - nums[n-1])

	for i := 1; i < n; i++ {
		maxAbs = max(maxAbs, abs(nums[i]-nums[i-1]))
	}

	return maxAbs
}
