func findIntersectionValues(nums1 []int, nums2 []int) []int {
	cacheNums1 := make(map[int]int)
	cacheNums2 := make(map[int]int)

	for _, n := range nums1 {
		cacheNums1[n] = 1
	}
	for _, n := range nums2 {
		cacheNums2[n] = 1
	}
	res1 := 0
	for _, n := range nums1 {
		res1 += cacheNums2[n]
	}

	res2 := 0
	for _, n := range nums2 {
		res2 += cacheNums1[n]
	}

	return []int{res1, res2}
}
