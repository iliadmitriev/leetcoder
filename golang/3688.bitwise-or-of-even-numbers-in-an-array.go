func evenNumberBitwiseORs(nums []int) int {
	x := 0

	for _, v := range nums {
		if v&1 == 0 {
			x |= v
		}
	}

	return x
}