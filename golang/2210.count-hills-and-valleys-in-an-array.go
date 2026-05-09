func countHillValley(nums []int) int {
	n := len(nums)
	cnt := 0

	for i, j, k := 0, 1, 2; k < n; k++ {
		if nums[j] == nums[k] {
			continue
		}

		if nums[i] < nums[j] && nums[j] > nums[k] {
			cnt++
		} else if nums[i] > nums[j] && nums[j] < nums[k] {
			cnt++
		}

		i, j = j, k
	}

	return cnt
}
