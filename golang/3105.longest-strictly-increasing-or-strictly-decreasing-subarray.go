func longestMonotonicSubarray(nums []int) int {
	N := len(nums)
	inc, dec := 1, 1
	longest := 1

	for i := 1; i < N; i++ {
		if nums[i-1] < nums[i] {
			inc++
			dec = 1
		} else if nums[i-1] > nums[i] {
			dec++
			inc = 1
		} else {
			inc = 1
			dec = 1
		}

		longest = max(longest, inc)
		longest = max(longest, dec)
	}

	return longest
}
