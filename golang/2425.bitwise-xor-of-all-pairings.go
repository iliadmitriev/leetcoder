func xorAllNums(nums1 []int, nums2 []int) int {
	odd1, odd2 := len(nums1)%2 == 1, len(nums2)%2 == 1

	ans := 0

	if odd2 {
		for _, num := range nums1 {
			ans ^= num
		}
	}

	if odd1 {
		for _, num := range nums2 {
			ans ^= num
		}
	}

	return ans
}
