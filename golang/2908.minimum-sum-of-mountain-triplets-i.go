func minimumSum(nums []int) int {
	n := len(nums)

	// left - prefix min, left[i] is a current left minimum to i
	// right - suffix min, right[i] is a current right minimum from i
	left, right := make([]int, n), make([]int, n)
	left[0] = nums[0]
	right[0] = nums[len(nums)-1]

	for i := 1; i < n; i++ {
		left[i] = min(left[i-1], nums[i])
		right[i] = min(right[i-1], nums[n-i-1])
	}

	INF := int(1e9)
	ans := INF

	for i := 1; i < n-1; i++ {
		if nums[i] > left[i] && nums[i] > right[n-i-1] {
			ans = min(ans, left[i]+nums[i]+right[n-i-1])
		}
	}

	if ans == INF {
		return -1
	}

	return ans
}
