
func addedInteger(nums1 []int, nums2 []int) int {
	x := minArrElement(nums2) - minArrElement(nums1)

	return x
}

func minArrElement(arr []int) int {
	x := arr[0]
	for i := range arr {
		if arr[i] < x {
			x = arr[i]
		}
	}

	return x
}
