func sumOfUnique(nums []int) int {
	counter := make(map[int]int)
	for _, num := range nums {
		counter[num]++
	}

	res := 0
	for k, v := range counter {
		if v == 1 {
			res += k
		}
	}

	return res
}
