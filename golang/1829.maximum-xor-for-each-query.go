func getMaximumXor(nums []int, maximumBit int) []int {
	n := len(nums)
	k := 1<<maximumBit - 1
	res := make([]int, n)

	allXor := 0

	for i := 0; i < n; i++ {
		allXor ^= nums[i]
		res[n-i-1] = allXor ^ k
	}

	return res
}
