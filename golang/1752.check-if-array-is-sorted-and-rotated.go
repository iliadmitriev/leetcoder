func check(nums []int) bool {
	prev := nums[0]
	rotations := 1

	// drop rotations if array is not rotated
	if nums[0] < nums[len(nums)-1] {
		rotations = 0
	}

	for _, num := range nums {
		if num < prev {
			rotations--
		}

		if rotations < 0 {
			return false
		}

		prev = num
	}

	return true
}
