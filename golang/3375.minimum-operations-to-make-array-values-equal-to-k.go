func minOperations(nums []int, k int) int {
	count := 0
	cache := make([]int, 101)

	for _, num := range nums {
		if num < k {
			return -1
		}

		if cache[num] == 0 {
			count++
		}
		cache[num]++
	}

	if cache[k] > 0 {
		return count - 1
	}

	return count
}
