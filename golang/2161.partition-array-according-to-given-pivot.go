func pivotArray(nums []int, pivot int) []int {
	n := len(nums)
	less := make([]int, 0, n)
	greater := make([]int, 0)
	piv := 0

	for i := 0; i < n; i++ {
		switch {
		case nums[i] < pivot:
			less = append(less, nums[i])
		case nums[i] > pivot:
			greater = append(greater, nums[i])
		default:
			piv++
		}
	}

	for ; piv > 0; piv-- {
		less = append(less, pivot)
	}

	less = append(less, greater...)
	return less
}
