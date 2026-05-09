func maxWidthRamp(nums []int) int {
	n := len(nums)

	maxPrefix := make([]int, n)
	curMax := nums[n-1]

	for i := n - 1; i >= 0; i-- {
		curMax = max(curMax, nums[i])
		maxPrefix[i] = curMax
	}

	ramp := 0
	j := 0

	for i := 0; i < n; i++ {
		if nums[i] > maxPrefix[i] {
			continue
		}

		for j < n && nums[i] <= maxPrefix[j] {
			j++
		}

		ramp = max(ramp, j-i-1)
	}

	return ramp
}
