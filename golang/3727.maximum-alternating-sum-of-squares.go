func maxAlternatingSum(nums []int) int64 {
	n := len(nums)
	h := n / 2

	for i := range n {
		nums[i] = nums[i] * nums[i]
	}

	slices.Sort(nums)

	left := 0
	for i := range h {
		left += nums[i]
	}

	right := 0
	for i := h; i < n; i++ {
		right += nums[i]
	}

	return int64(right - left)
}