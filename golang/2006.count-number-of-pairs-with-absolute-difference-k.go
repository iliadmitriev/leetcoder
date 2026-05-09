func countKDifference(nums []int, k int) int {
	cache := make(map[int]int)
	count := 0

	for _, num := range nums {
		count += cache[num-k] + cache[num+k]
		cache[num]++
	}

	return count
}
