func findSubarrays(nums []int) bool {
	sub := make(map[int]bool)

	for i := 0; i < len(nums)-1; i++ {
		d := nums[i] + nums[i+1]

		if _, ok := sub[d]; ok {
			return true
		}

		sub[d] = true
	}

	return false
}
