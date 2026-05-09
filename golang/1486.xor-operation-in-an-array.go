func xorOperation(n int, start int) int {
	res := 0

	for i := range n {
		res ^= start + 2*i
	}

	return res
}
