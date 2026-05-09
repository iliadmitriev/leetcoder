func isHappy(n int) bool {
	s := make(map[int]bool)
	var n2, x int

	for n != 1 {

		n2 = 0

		for n > 0 {
			x = n % 10
			n /= 10

			n2 += x * x
		}

		n = n2

		if _, ok := s[n]; ok {
			return false
		}

		s[n] = true

	}

	return true
}
