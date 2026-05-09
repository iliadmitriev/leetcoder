func maximumSubarraySum(nums []int, k int) int64 {
	n := len(nums)
	curWindow := make(map[int]int, n)
	curSum := 0

	maxSumWin := 0

	for i := 0; i < n; i++ {
		curSum += nums[i]
		curWindow[nums[i]]++

		if i >= k {
			curSum -= nums[i-k]
			curWindow[nums[i-k]]--

			if curWindow[nums[i-k]] == 0 {
				delete(curWindow, nums[i-k])
			}
		}

		if i >= k-1 && k == len(curWindow) {
			maxSumWin = max(maxSumWin, curSum)
		}

	}

	return int64(maxSumWin)
}
