func maximumSwap(num int) int {
	st := make([]int, 0, 10)
	for num > 0 {
		st = append(st, num%10)
		num /= 10
	}

	maxPos := make([]int, 0, len(st))
	curMax, curIdx := st[0], 0
	for i := 0; i < len(st); i++ {
		if st[i] > curMax {
			curMax = st[i]
			curIdx = i
		}
		maxPos = append(maxPos, curIdx)
	}

	for i := len(st) - 1; i > 0; i-- {
		if st[i] < st[maxPos[i]] {
			st[maxPos[i]], st[i] = st[i], st[maxPos[i]]
			break
		}
	}

	for len(st) > 0 {
		num *= 10
		num += st[len(st)-1]
		st = st[:len(st)-1]
	}
	return num
}
