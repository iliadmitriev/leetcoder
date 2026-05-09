func minOperations(nums []int) int {
	ops := 0
	value := nums[0]

	for i := 1; i < len(nums); i++ {
		if nums[i] > value {
			value = nums[i]
		} else {
			value++
			ops += value - nums[i]
		}
	}

	return ops
}
