func pivotInteger(n int) int {
	prefix, suffix := 0, n*(n+1)/2

	for i := 1; i <= n; i++ {
		prefix += i
		if prefix == suffix {
			return i
		}

		suffix -= i
	}

	return -1
}
