func longestNiceSubarray(nums []int) int {
	mask := 0xffffffff
	maxLen := 0
	left := 0

	for right := 0; right < len(nums); right++ {
		mask ^= nums[right]

		for mask&nums[right] > 0 {
			mask ^= nums[left]
			left++
		}

		maxLen = max(maxLen, right-left+1)
	}

	return maxLen
}
