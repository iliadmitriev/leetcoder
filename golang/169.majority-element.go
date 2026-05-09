func majorityElement(nums []int) int {
	count := 0
	maj := -1

	for _, num := range nums {
		if count == 0 {
			maj = num
		}

		if maj == num {
			count++
		} else {
			count--
		}
	}

	return maj
}