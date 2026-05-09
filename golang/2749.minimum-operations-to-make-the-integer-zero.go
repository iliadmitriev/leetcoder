func makeTheIntegerZero(num1 int, num2 int) int {
	x := 0

	for k := 1; k < 33; k++ {
		x = num1 - k*num2

		if x < k {
			return -1
		}

		if bits.OnesCount(uint(x)) <= k {
			return k
		}
	}

	return -1
}
