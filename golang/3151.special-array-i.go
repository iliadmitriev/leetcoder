func isArraySpecial(nums []int) bool {
	parity := 1 - nums[0]%2
	n := len(nums)

	for i := 1; i < n; i++ {
		if (nums[i] % 2) != parity {
			return false
		}

		parity = 1 - parity
	}

	return true
}
