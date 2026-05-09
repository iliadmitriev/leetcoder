func minOperations(nums []int) int {
	N := len(nums)
	ops := 0

	for i := 0; i < N-2; i++ {
		if nums[i] == 1 {
			continue
		}

		ops++

		nums[i] = nums[i] ^ 1
		nums[i+1] = nums[i+1] ^ 1
		nums[i+2] = nums[i+2] ^ 1
	}

	if nums[N-2] == 0 || nums[N-1] == 0 {
		return -1
	}

	return ops
}
