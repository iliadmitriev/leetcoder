
func absInt(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func maxAbsoluteSum(nums []int) int {
	maxSum, minSum := 0, 0
	curMinSum, curMaxSum := 0, 0

	for _, num := range nums {
		curMinSum = min(0, curMinSum+num)
		curMaxSum = max(0, curMaxSum+num)

		minSum = min(minSum, curMinSum)
		maxSum = max(maxSum, curMaxSum)

	}

	return max(absInt(maxSum), absInt(minSum))
}
