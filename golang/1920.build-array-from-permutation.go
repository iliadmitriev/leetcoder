func buildArray(nums []int) []int {
	res := make([]int, len(nums))
	for i, num := range nums {
		res[i] = nums[num]
	}

	return res
}
