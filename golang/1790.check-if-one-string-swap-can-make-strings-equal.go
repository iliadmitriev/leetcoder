func areAlmostEqual(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}

	N := len(s1)
	swaps := 2
	ind := -1

	for i := 0; i < N; i++ {
		if s1[i] == s2[i] {
			continue
		}

		swaps--
		if swaps < 0 {
			return false
		}

		if ind < 0 {
			ind = i
			continue
		}

		if s1[ind] != s2[i] || s1[i] != s2[ind] {
			return false
		}
	}

	return swaps == 0 || swaps == 2
}
