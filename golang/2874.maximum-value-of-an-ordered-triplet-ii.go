func maximumTripletValue(nums []int) int64 {
	res := 0
	prefix, diff := 0, 0

	for _, num := range nums {
		res = max(res, diff*num)
		prefix = max(prefix, num)
		diff = max(diff, prefix-num)
	}

	return int64(res)
}
