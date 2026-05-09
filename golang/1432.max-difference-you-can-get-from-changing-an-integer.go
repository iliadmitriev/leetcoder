func maxDiff(num int) int {
	value := make([]int, 0)

	for num > 0 {
		value = append(value, num%10)
		num /= 10
	}

	// a: default most significant digit change to 9
	// b: default most significant digit change to 1
	aSrc, aDst := value[len(value)-1], 9
	bSrc, bDst := value[len(value)-1], 1

	// a: if first is 9, then look for better candidate
	for i := len(value) - 1; i >= 0; i-- {
		if value[i] < 9 {
			aSrc = value[i]
			break
		}
	}

	// b: if first is 1, then look for better candidate and set to 0 (instead of 1)
	if bSrc == 1 {
		for i := len(value) - 1; i >= 0; i-- {
			if value[i] > 1 {
				bSrc = value[i]
				bDst = 0
				break
			}
		}
	}

	a, b := 0, 0

	for len(value) > 0 {
		v := value[len(value)-1]     // back
		value = value[:len(value)-1] // pop

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
