func maximumDifference(nums []int) int {
	maxDiff := -1
	curMin := nums[0]

	for _, num := range nums {
		curMin = min(curMin, num)
		maxDiff = max(maxDiff, num-curMin)
	}

	if maxDiff == 0 {
		return -1
	}

	return maxDiff
}
