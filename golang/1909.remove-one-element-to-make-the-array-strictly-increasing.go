func canBeIncreasing(nums []int) bool {
	deletions := 0

	for i := 1; i < len(nums); i++ {
		if nums[i-1] < nums[i] {
			continue
		}
		deletions++
		if deletions > 1 {
			return false
		}
		if i > 1 && nums[i-2] >= nums[i] {
			nums[i] = nums[i-1]
		} else {
			nums[i-1] = nums[i]
		}
	}

	return deletions < 2
}
