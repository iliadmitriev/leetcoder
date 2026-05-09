func missingNumber(nums []int) int {
	res := 0
	n := len(nums)

	for i := 0; i < n; i++ {
		res ^= nums[i] ^ i
	}

	return res ^ n
}
