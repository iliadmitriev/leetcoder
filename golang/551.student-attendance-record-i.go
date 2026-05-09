func checkRecord(s string) bool {
	a, l := 0, 0

	for _, v := range s {
		switch v {
		case 'A':
			a++
			l = 0
		case 'L':
			l++
		default:
			l = 0
		}

		if a >= 2 || l >= 3 {
			return false
		}
	}

	return true
}
