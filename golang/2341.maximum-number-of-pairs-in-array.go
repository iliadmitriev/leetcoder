func numberOfPairs(nums []int) []int {
	const N = 101
	pairs := make([]int, N)

	for _, num := range nums {
		pairs[num]++
	}

	res := make([]int, 2)

	for _, p := range pairs {
		res[0] += p / 2
		res[1] += p % 2
	}

	return res
}
