func leftRightDifference(nums []int) []int {
	n := len(nums)
	left, right := make([]int, n), make([]int, n)

	for i := 1; i < n; i++ {
		left[i] = left[i-1] + nums[i-1]
		right[n-i-1] = right[n-i] + nums[n-i]
	}

	for i := 0; i < n; i++ {
		if left[i] > right[i] {
			nums[i] = left[i] - right[i]
		} else {
			nums[i] = right[i] - left[i]
		}
	}

	return nums
}
