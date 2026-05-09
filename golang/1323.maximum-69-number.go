func maximum69Number(num int) int {
	pos := -1

	for x, i := num, 0; x > 0; x, i = x/10, i+1 {
		if x%10 == 6 {
			pos = i
		}
	}

	if pos == -1 {
		return num
	}

	p := 3
	for range pos {
		p *= 10
	}

	return num + p
}
