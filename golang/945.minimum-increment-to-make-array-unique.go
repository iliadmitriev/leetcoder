func minIncrementForUnique(nums []int) int {
	sort.Ints(nums)
	ans := 0
	prev := -1

	for _, num := range nums {
		if prev < num {
			prev = num
			continue
		}

		ans += prev - num + 1
		prev++
	}

	return ans
}
