func firstStableIndex(nums []int, k int) int {
	n := len(nums)
	vmax := make([]int, n)
	vmax[0] = nums[0]
	for i := 1; i < n; i++ {
		vmax[i] = max(vmax[i-1], nums[i])
	}

	vmin := make([]int, n)
	vmin[n-1] = nums[n-1]
	for i := n - 2; i >= 0; i-- {
		vmin[i] = min(vmin[i+1], nums[i])
	}

	for i := range n {
		if vmax[i]-vmin[i] <= k {
			return i
		}
	}

	return -1
}