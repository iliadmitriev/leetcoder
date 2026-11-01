func minMoves(nums []int) int {
	total := 0
	minimal := nums[0]

	for _, v := range nums {
		minimal = min(minimal, v)
		total += v
	}

	return total - len(nums)*minimal
}