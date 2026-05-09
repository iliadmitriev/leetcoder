func minMaxDifference(num int) int {
	value := make([]int, 0)

	for num > 0 {
		value = append(value, num%10)
		num /= 10
	}

	aSrc, aDst := value[len(value)-1], 9
	bSrc, bDst := value[len(value)-1], 0

	// look for better candidate for a
	for i := len(value) - 1; i >= 0; i-- {
		if value[i] < 9 {
			aSrc = value[i]
			break
		}
	}

	a, b := 0, 0

	for i := len(value) - 1; i >= 0; i-- {
		v := value[i]

		a *= 10
		b *= 10

		if v == aSrc {
			a += aDst
		} else {
			a += v
		}

		if v == bSrc {
			b += bDst
		} else {
			b += v
		}
	}

	return a - b
}
