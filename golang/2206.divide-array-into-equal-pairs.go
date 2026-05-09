func divideArray(nums []int) bool {
	cache := make([]int, 501)
	for _, num := range nums {
		cache[num]++
	}

	for _, val := range cache {
		if val%2 == 1 {
			return false
		}
	}

	return true
}
