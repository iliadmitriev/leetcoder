func maxIncreasingSubarrays(nums []int) int {
	n := len(nums)
	prev, cur := 0, 1
	maxLen := 0

	for i := 1; i < n; i++ {
		if nums[i-1] < nums[i] {
			cur++
		} else {
			prev = cur
			cur = 1
		}

		maxLen = max(maxLen, min(prev, cur))
		maxLen = max(maxLen, cur/2)
	}

	return maxLen
}
