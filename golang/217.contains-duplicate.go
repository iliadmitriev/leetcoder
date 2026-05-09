func containsDuplicate(nums []int) bool {
	cache := make(map[int]bool, len(nums))

	for _, num := range nums {
		if _, ok := cache[num]; ok {
			return true
		}

		cache[num] = true
	}

	return false
}
