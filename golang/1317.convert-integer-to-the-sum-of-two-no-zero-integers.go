func getNoZeroIntegers(n int) []int {
	a, b := 0, 0

	for p := 1; n > 0; p *= 10 {
		d := n % 10
		n /= 10

		// if d is 2-9 or it's a last digit (there is no carry available, in this case it can't be 0)
		if d >= 2 || n == 0 {
			a += p * 1
			b += p * (d - 1)
		} else { // 0 or 1
			n--              // get carry 10, so it will be 10 or 11
			a += p * (d + 1) // 0 or 1
			b += p * 9
		}

	}

	return []int{a, b}
}
