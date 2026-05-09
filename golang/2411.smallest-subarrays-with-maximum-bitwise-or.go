func smallestSubarrays(nums []int) []int {
	n := len(nums)
	res := make([]int, n)

	for i := range n {
		res[i] = 1
		j := i - 1
		x := nums[i]

		for j >= 0 && x|nums[j] != nums[j] {
			res[j] = i - j + 1
			nums[j] |= x
			j--
		}
	}

	return res
}
