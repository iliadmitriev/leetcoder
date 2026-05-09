func sumIndicesWithKSetBits(nums []int, k int) int {
	total := 0

	for i, num := range nums {
		if k == popCount(i) {
			total += num
		}
	}

	return total
}

// popCount returns the number of 1 bits in the binary representation of n
func popCount(n int) int {
	count := 0

	for n > 0 {
		n &= n - 1
		count++
	}

	return count
}
