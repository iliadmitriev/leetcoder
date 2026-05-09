func hasIncreasingSubarrays(nums []int, k int) bool {
	n := len(nums)
	cur, prev := 1, 0

	for i := 1; i < n; i++ {
		if nums[i-1] < nums[i] {
			cur++
		} else {
			prev = cur
			cur = 1
		}

		if (cur >= k && prev >= k) || cur >= 2*k {
			return true
		}
	}

	return false
}
