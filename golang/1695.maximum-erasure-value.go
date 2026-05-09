func maximumUniqueSubarray(nums []int) int {
	maxUniq := 0

	cur, j := 0, 0
	win := make(map[int]int, len(nums))

	for _, num := range nums {
		cur += num
		win[num]++

		for win[num] > 1 {
			cur -= nums[j]
			win[nums[j]]--
			j++
		}

		maxUniq = max(maxUniq, cur)
	}

	return maxUniq
}
