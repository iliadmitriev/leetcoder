func prefixesDivBy5(nums []int) []bool {
	cur := 0
	res := make([]bool, 0, len(nums))

	for _, v := range nums {
		cur = (cur << 1) + v
		cur %= 5
		res = append(res, cur == 0)
	}

	return res
}
