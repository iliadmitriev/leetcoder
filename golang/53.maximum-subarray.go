import "math"

func maxSubArray(nums []int) int {
	maxSum := math.MinInt
	curMaxSum := 0

	for _, num := range nums {
		curMaxSum += num

		maxSum = max(maxSum, curMaxSum)
		curMaxSum = max(0, curMaxSum)
	}

	return maxSum
}
