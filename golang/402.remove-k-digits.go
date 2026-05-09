func removeKdigits(num string, k int) string {
	st := make([]byte, 0, len(num))

	for i := 0; i < len(num); i++ {
		for k > 0 && len(st) > 0 && num[i] < st[len(st)-1] {
			st = st[:len(st)-1]
			k--
		}

		if len(st) > 0 || num[i] != '0' {
			st = append(st, num[i])
		}
	}

	st = st[:max(0, len(st)-k)]
	if len(st) == 0 {
		return "0"
	}

	return string(st)
}
