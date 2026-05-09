func getSneakyNumbers(nums []int) []int {
	sneaky := make([]int, 0, 2)

	n := len(nums)
	cache := make([]uint8, n-2)

	for _, num := range nums {
		if cache[num] > 0 {
			sneaky = append(sneaky, num)
		}

		cache[num]++
	}

	return sneaky
}
