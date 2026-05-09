func firstMissingPositive(nums []int) int {
	n := len(nums)
	// get rid of zero and negative numbers, set them to n + 1 (max possible answer)
	for i := 0; i < n; i++ {
		if nums[i] <= 0 {
			nums[i] = n + 1
		}
	}

	// a possible answer is within the range of [1, n]
	// iterate array and if number is in the range, set it to negative
	for i := 0; i < n; i++ {
		idx := abs(nums[i]) - 1
		if idx >= 0 && idx < n {
			nums[idx] = -abs(nums[idx])
		}
	}

	// find first positive number
	for i := 1; i <= n; i++ {
		if nums[i-1] >= 0 {
			return i
		}
	}

	return n + 1
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}