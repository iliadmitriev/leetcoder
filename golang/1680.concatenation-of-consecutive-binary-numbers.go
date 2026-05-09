func concatenatedBinary(n int) int {
	MOD := int(1e9) + 7

	v := 0
	shift := 0

	for i := 1; i <= n; i++ {
		if (i & (i - 1)) == 0 {
			shift++
		}

		v = (v << shift) | i
		v %= MOD
	}

	return v
}