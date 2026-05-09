func checkValidString(s string) bool {
	left_min, left_max := 0, 0

	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			left_min++
			left_max++
		} else if s[i] == ')' {
			if left_min > 0 {
				left_min--
			}
			left_max--
		} else {
			if left_min > 0 {
				left_min--
			}
			left_max++
		}

		if left_max < 0 {
			return false
		}
	}

	return left_min == 0
}
