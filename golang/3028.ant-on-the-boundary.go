func returnToBoundaryCount(nums []int) int {
	ans := 0
	pos := 0

	for _, num := range nums {
		pos += num
		if pos == 0 {
			ans++
		}
	}

	return ans
}
