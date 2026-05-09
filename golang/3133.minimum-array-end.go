func minEnd(n int, x int) int64 {
	mask := x
	n--

	for i := 0; n > 0; i++ {
		if mask&1 == 0 {
			x |= (n & 1) << i
			n >>= 1
		}

		mask >>= 1
	}
	return int64(x)
}
