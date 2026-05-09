func freqAlphabets(s string) string {
	tmp := make([]rune, 0, len(s))
	res := strings.Builder{}

	for _, ch := range s {
		if ch == '#' {
			n := len(tmp)
			a, b := tmp[n-2], tmp[n-1]
			tmp = tmp[:n-2]
			tmp = append(tmp, a*10+b)
		} else {
			tmp = append(tmp, ch-'0')
		}
	}

	for _, v := range tmp {
		res.WriteRune('a' + v - 1)
	}

	return res.String()
}
