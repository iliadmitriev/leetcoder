func findKOr(nums []int, k int) int {
	res := 0

	for i := 0; i < 32; i++ {
		c := k

		for j := 0; j < len(nums); j++ {
			if nums[j]&(1<<i) != 0 {
				c--
			}

			if c == 0 {
				res |= 1 << i
				break
			}
		}
	}

	return res
}
