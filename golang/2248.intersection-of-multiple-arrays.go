import "sort"

func intersection(nums [][]int) []int {
	res := nums[0]
	sort.Ints(res)

	for i := 1; i < len(nums); i++ {
		sort.Ints(nums[i])
		res = __intersect(res, nums[i])

		if len(res) == 0 {
			break
		}
	}

	return res
}

func __intersect(nums1, nums2 []int) []int {
	k := 0

	for i, j := 0, 0; i < len(nums1) && j < len(nums2); {
		if nums1[i] < nums2[j] {
			i++
		} else if nums1[i] > nums2[j] {
			j++
		} else {
			nums1[k] = nums1[i]
			j++
			i++
			k++
		}
	}

	return nums1[:k]
}
