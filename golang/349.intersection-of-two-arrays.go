import (
	"sort"
)

func intersection(nums1 []int, nums2 []int) []int {
	sort.Ints(nums1)
	sort.Ints(nums2)

	m, n := len(nums1), len(nums2)
	i, j := 0, 0
	prev := -1
	res := make([]int, 0, min(n, m))

	for i < m && j < n {
		if nums1[i] < nums2[j] {
			i++
		} else if nums1[i] > nums2[j] {
			j++
		} else {
			if prev != nums1[i] {
				res = append(res, nums1[i])
			}
			prev = nums1[i]
			i++
			j++
		}
	}

	return res
}