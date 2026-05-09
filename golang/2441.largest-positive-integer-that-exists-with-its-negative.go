func findMaxK(nums []int) int {
	cache := make([]bool, 2001)
	res := -1

	for _, num := range nums {
		if cache[1000-num] {
			if res < absFunc(num) {
				res = absFunc(num)
			}
		}
		cache[num+1000] = true
	}

	return res
}

func absFunc(x int) int {
	if x < 0 {
		return -x
	}

	return x
}
