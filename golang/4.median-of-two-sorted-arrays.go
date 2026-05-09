func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	m, n := len(nums1), len(nums2)
	tmp := make([]int, m+n)

	i, j := 0, 0
	k := 0

	for i < m && j < n {
		if nums1[i] < nums2[j] {
			tmp[k] = nums1[i]
			i++
		} else {
			tmp[k] = nums2[j]
			j++
		}
		k++
	}

	for i < m {
		tmp[k] = nums1[i]
		i++
    k++
	}

	for j < n {
		tmp[k] = nums2[j]
		j++
    k++
	}

	p := m + n
	if p%2 == 0 {
		return float64(tmp[p/2 - 1]+tmp[p/2]) / 2.0
	}

	return float64(tmp[p/2])
}