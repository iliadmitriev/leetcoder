func sumOfSquares(nums []int) int {
	res := 0

	n := len(nums)

	for i, num := range nums {
		if n%(i+1) == 0 {
			res += num * num
		}
	}

	return res
}
