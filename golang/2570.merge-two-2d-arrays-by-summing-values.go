func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
	m, n := len(nums1), len(nums2)
	res := make([][]int, 0, max(m, n))
	i, j := 0, 0

	for i < m && j < n {
		switch {
		case nums1[i][0] < nums2[j][0]:
			res = append(res, []int{nums1[i][0], nums1[i][1]})
			i++
		case nums1[i][0] > nums2[j][0]:
			res = append(res, []int{nums2[j][0], nums2[j][1]})
			j++
		default:
			res = append(res, []int{nums1[i][0], nums1[i][1] + nums2[j][1]})
			i++
			j++
		}
	}

	res = append(res, nums1[i:]...)
	res = append(res, nums2[j:]...)

	return res
}
