func singleNumber(nums []int) []int {
	first, second := 0, 0

	for _, num := range nums {
		first ^= num
	}

	mask := first & (^first + 1)

	for _, num := range nums {
		if num&mask == 0 {
			second ^= num
		}
	}

	return []int{first ^ second, second}
}
