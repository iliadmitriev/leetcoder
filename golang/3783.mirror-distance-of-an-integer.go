func mirrorDistance(n int) int {
	rev := func(x int) int {
		res := 0

		for ; x > 0; x /= 10 {
			res = res*10 + x%10
		}

		return res
	}

	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	return abs(n - rev(n))
}
