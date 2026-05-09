
func countPartitions(nums []int) int {
	n := len(nums)
	count := 0
	left := 0
	right := 0

	for _, num := range nums {
		right += num
	}

	for i := range n - 1 {
		left += nums[i]
		right -= nums[i]

		if (left-right)%2 == 0 {
			count++
		}
	}

	return count
}
