func subarraysDivByK(nums []int, k int) int {
	res := 0

	acc := 0
	seen := map[int]int{0: 1}

	for _, num := range nums {
		acc += num
		acc %= k
		acc = (acc + k) % k
		res += seen[acc]
		seen[acc]++
	}

	return res
}
