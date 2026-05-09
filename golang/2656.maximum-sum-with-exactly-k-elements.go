func maximizeSum(nums []int, k int) int {
	first := nums[0]
	for _, n := range nums {
		first = max(first, n)
	}

	last := first + k - 1

	return (first + last) * k / 2
}
