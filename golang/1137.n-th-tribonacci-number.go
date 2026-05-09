func tribonacci(n int) int {
	if n == 0 {
		return 0
	}

	if n == 1 || n == 2 {
		return 1
	}

	res, t0, t1, t2 := 0, 0, 1, 1

	for i := 2; i < n; i++ {
		res = t0 + t1 + t2
		t0, t1, t2 = t1, t2, res
	}

	return res
}
