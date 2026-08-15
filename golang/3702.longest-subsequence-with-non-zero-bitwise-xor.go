func longestSubsequence(nums []int) int {
	nonZero := 0
	all := 0

	for _, v := range nums {
		all ^= v

		if v != 0 {
			nonZero++
		}
	}

	// if there is no non-zero elements
	// can't collect non-empty subsequence
	if nonZero == 0 {
		return 0
	}

	// if XORing all elements returns 0
	// and there is non zero elements
	// then dropping only one yields in non zero sequence
	if all == 0 {
		return len(nums) - 1
	}

	return len(nums)
}