func countBadPairs(nums []int) int64 {
	var res int
	mp := make(map[int]int)
	N := len(nums)

	for i, num := range nums {
		mp[num-i]++
	}

	for _, v := range mp {
		res += v * (N - v)
	}

	return int64(res / 2)
}
