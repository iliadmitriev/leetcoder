func longestSquareStreak(nums []int) int {
	const limit = int(1e5)

	cache := make(map[int]bool, len(nums))
	seen := make(map[int]bool)

	for _, num := range nums {
		cache[num] = true
	}

	maxLen := 0

	for _, num := range nums {
		if _, ok := seen[num]; ok {
			continue
		}
		seen[num] = true

		cur := num
		curLen := 1

		for cur*cur <= limit && cache[cur*cur] {
			cur *= cur
			curLen++
		}

		if curLen > maxLen {
			maxLen = curLen
		}
	}

	if maxLen < 2 {
		return -1
	}

	return maxLen
}
