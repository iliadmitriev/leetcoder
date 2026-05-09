func twoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
	const N = 101
	set1, set2, set3 := make([]int, N), make([]int, N), make([]int, N)

	for _, num := range nums1 {
		set1[num] = 1
	}

	for _, num := range nums2 {
		set2[num] = 1
	}

	for _, num := range nums3 {
		set3[num] = 1
	}

	res := make([]int, 0)
	for i := 0; i < N; i++ {
		if set1[i]+set2[i]+set3[i] > 1 {
			res = append(res, i)
		}
	}

	return res
}
