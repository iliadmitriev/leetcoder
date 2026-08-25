func missingMultiple(nums []int, k int) int {
  /*
  Time: O(n)
  Space: O(1)
  */
	const N = 5
	s := make([]uint64, 5)

	for _, n := range nums {
		if n%k != 0 {
			continue
		}

		pos := n/k - 1
		i, j := pos/64, pos%64

		s[i] |= 1 << j
	}

	for i, v := range s {
		if v == math.MaxUint64 {
			continue
		}

		j := bits.TrailingZeros64(^v)
		pos := i*64 + j + 1

		return pos * k
	}

	return k
}