func smallestIndex(nums []int) int {
	digits := func(x int) int {
		y := 0
		for x > 0 {
			y += x % 10
			x /= 10
		}
		return y
	}

	for i, x := range nums {
		if i == digits(x) {
			return i
		}
	}

	return -1
}