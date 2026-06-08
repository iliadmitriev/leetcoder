func pivotArray(nums []int, pivot int) []int {
	n := len(nums)

	res := make([]int, n)

	// write pointers
	l, r := 0, n-1

	// read pointers
	for i, j := 0, n-1; i < n; i, j = i+1, j-1 {
		if nums[i] < pivot {
			res[l] = nums[i]
			l++
		}

		if nums[j] > pivot {
			res[r] = nums[j]
			r--
		}
	}

	// fill the gap
	for i := l; i <= r; i++ {
		res[i] = pivot
	}

	return res
}