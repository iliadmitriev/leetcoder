func countGood(nums []int, k int) int64 {
	n := len(nums)
	res := 0
	pairs := 0
	win := make(map[int]int)

	for left, right := 0, 0; right < n; right++ {
		pairs += win[nums[right]]
		win[nums[right]]++

		for pairs >= k {
			win[nums[left]]--
			pairs -= win[nums[left]]

			left++
		}

		res += left
	}

	return int64(res)
}
