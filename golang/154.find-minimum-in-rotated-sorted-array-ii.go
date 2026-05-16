func findMin(nums []int) int {
	lo, hi := 0, len(nums)-1

	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		switch {
		case nums[mid] > nums[hi]:
			lo = mid + 1
		case nums[mid] < nums[hi]:
			hi = mid
		default:
			hi--
		}
	}

	return nums[lo]
}