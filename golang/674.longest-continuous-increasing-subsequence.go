func findLengthOfLCIS(nums []int) int {
	maxLength := 1
	length := 1
	n := len(nums)

	for i := 1; i < n; i++ {
		if nums[i-1] < nums[i] {
			length++
		} else {
			length = 1
		}

		maxLength = max(maxLength, length)
	}

	return maxLength
}
