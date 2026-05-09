func longestSubarray(nums []int) int {
	longest := 0
	count := 0
	prev := -1

	for _, num := range nums {
		if num == prev {
			count++
			if count > longest {
				longest = count
			}
		} else if num > prev {
			prev = num
			count = 1
			longest = 1
		} else {
			count = 0
		}
	}

	return longest
}
