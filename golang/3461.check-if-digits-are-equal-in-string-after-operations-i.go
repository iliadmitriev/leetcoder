func hasSameDigits(s string) bool {
	n := len(s)
	v := make([]int, n)

	for i, ch := range s {
		v[i] = int(ch - '0')
	}

	for i := range n - 2 {
		for j := range n - 1 - i {
			v[j] = (v[j] + v[j+1]) % 10
		}
	}

	return v[0] == v[1]
}
