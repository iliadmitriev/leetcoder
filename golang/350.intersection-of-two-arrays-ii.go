func intersect(nums1 []int, nums2 []int) []int {
	res := []int{}
  sort.Ints(nums1)
  sort.Ints(nums2)

	n, m := len(nums1), len(nums2)

	for i, j := 0, 0; i < n && j < m; {
		if nums1[i] < nums2[j] {
			i++
		} else if nums1[i] > nums2[j] {
			j++
		} else {
			res = append(res, nums1[i])
			i++
			j++
		}
	}

	return res
}