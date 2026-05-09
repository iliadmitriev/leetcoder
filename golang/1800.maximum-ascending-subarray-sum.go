func maxAscendingSum(nums []int) int {
	currSum, maxSum := 0, 0
	prev := 0

	for _, num := range nums {
		if prev < num {
			currSum += num
		} else {
			currSum = num
		}

		prev = num
		if currSum > maxSum {
			maxSum = currSum
		}
	}

	return maxSum
}
