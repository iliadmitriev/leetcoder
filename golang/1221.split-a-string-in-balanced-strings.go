func balancedStringSplit(s string) int {
	res := 0
	balance := 0

	for _, c := range s {
		if c == 'L' {
			balance++
		} else {
			balance--
		}

		if balance == 0 {
			res++
		}
	}

	return res
}
