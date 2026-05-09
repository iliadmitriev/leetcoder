func longestOnes(nums []int, k int) int {
	n := len(nums)
	maxLen := 0
	zero := 0
	i, j := 0, 0

	for ; i < n; i++ {
		if nums[i] == 0 {
			zero++
		}

		for zero > k && j <= i {
			if nums[j] == 0 {
				zero--
			}
			j++
		}

		maxLen = max(maxLen, i-j+1)
	}

	return maxLen
}