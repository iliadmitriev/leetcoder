func getConcatenation(nums []int) []int {
	n := len(nums)
	ans := make([]int, 0, 2*n)

	ans = append(ans, nums...)
	ans = append(ans, nums...)

	return ans
}
