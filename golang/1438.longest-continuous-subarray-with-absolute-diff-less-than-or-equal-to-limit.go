
func longestSubarray(nums []int, limit int) int {
	n := len(nums)
	increasing := make([]int, 0, n)
	decreasing := make([]int, 0, n)

	left := 0

	for i := 0; i < n; i++ {

		for len(increasing) > 0 && increasing[len(increasing)-1] > nums[i] {
			increasing = increasing[:len(increasing)-1]
		}

		for len(decreasing) > 0 && decreasing[len(decreasing)-1] < nums[i] {
			decreasing = decreasing[:len(decreasing)-1]
		}

		increasing = append(increasing, nums[i])
		decreasing = append(decreasing, nums[i])

		if decreasing[0]-increasing[0] > limit {
			if increasing[0] == nums[left] {
				increasing = increasing[1:]
			}

			if decreasing[0] == nums[left] {
				decreasing = decreasing[1:]
			}

			left++
		}
	}

	return n - left
}
