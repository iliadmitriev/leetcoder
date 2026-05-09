func constructTransformedArray(nums []int) []int {
	n := len(nums)
	res := make([]int, n)

	for i, num := range nums {
		res[i] = nums[(100*n+i+num)%n]
	}

	return res
}