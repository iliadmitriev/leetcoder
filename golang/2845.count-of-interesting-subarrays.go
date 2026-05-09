func countInterestingSubarrays(nums []int, modulo int, k int) int64 {
	total, prefix := 0, 0
	cache := make(map[int]int)

	cache[0] = 1

	for _, num := range nums {
		if num%modulo == k {
			prefix += 1
		}

		left := (prefix - k + modulo) % modulo
		total += cache[left]
		cache[prefix%modulo]++
	}

	return int64(total)
}
