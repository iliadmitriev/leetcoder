func waysToSplitArray(nums []int) int {
	left, right := 0, 0
	for _, num := range nums {
		right += num
	}

	count := 0

	for i := 0; i < len(nums)-1; i++ {
		left += nums[i]
		right -= nums[i]

		if left >= right {
			count++
		}
	}

	return count
}
