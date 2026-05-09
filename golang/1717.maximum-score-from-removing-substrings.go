
func getMaximumGain(s string, cha, chb rune, x int, y int) int {
	ch1, ch2 := 0, 0
	res := 0

	for _, ch := range s {
		switch ch {
		case cha:
			ch1++
		case chb:
			if ch1 > 0 {
				ch1--
				res += x
			} else {
				ch2++
			}
		default:
			res += y * min(ch1, ch2)
			ch1, ch2 = 0, 0
		}
	}

	res += y * min(ch1, ch2)

	return res
}

func maximumGain(s string, x int, y int) int {
	if x > y {
		return getMaximumGain(s, 'a', 'b', x, y)
	}
	return getMaximumGain(s, 'b', 'a', y, x)
}
