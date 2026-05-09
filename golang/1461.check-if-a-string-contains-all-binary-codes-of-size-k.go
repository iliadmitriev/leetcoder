func hasAllCodes(s string, k int) bool {
	target := 1 << k   // 0010 0000
	mask := target - 1 // 0001 1111
	n := len(s)

	// not enough digits to fulfill target
	if n-k+1 < mask {
		return false
	}

	acc := make([]bool, target)

	cur := 0      // current value
	dis := target // number of distinct values to collect

	for i, d := range s {
		// remove leftmost digit
		cur <<= 1
		cur &= mask

		// add rightmost digit
		if d == '1' {
			cur |= 1
		}

		// value have to be atmost k digits
		if i+1 < k {
			continue
		}

		// remove distinct count and add current value to accumulator
		if !acc[cur] {
			dis--
		}

		// not enough digits left to fulfill rest of the distinct values
		if n-i-1 < dis {
			return false
		}

		acc[cur] = true

		// early return
		if dis == 0 {
			return true
		}
	}

	return dis == 0
}