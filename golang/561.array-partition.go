func arrayPairSum(nums []int) int {
	total := 0
	n := len(nums)

	sort.Ints(nums)

	for i := 0; i < n; i += 2 {
		total += nums[i]
	}

	return total
}
