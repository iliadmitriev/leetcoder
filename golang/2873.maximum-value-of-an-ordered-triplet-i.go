func maximumTripletValue(nums []int) int64 {
	n := len(nums)
	result := 0
	prefix := make([]int, n)
	suffix := make([]int, n)

	prefix[0] = nums[0]
	for i := 1; i < n; i++ {
		prefix[i] = max(prefix[i-1], nums[i])
	}

	suffix[n-1] = nums[n-1]
	for i := n - 2; i >= 0; i-- {
		suffix[i] = max(suffix[i+1], nums[i])
	}

	for i := 1; i < n-1; i++ {
		result = max(result, (prefix[i-1]-nums[i])*suffix[i+1])
	}

	return int64(result)
}
