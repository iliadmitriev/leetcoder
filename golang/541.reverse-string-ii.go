func reverseStr(s string, k int) string {
	st := []byte(s)
	n := len(st)
	var m int

	for i := 0; i < n; i += 2 * k {

		m = min(i+k, n)

		for j := 0; j < (m-i)/2; j++ {
			st[i+j], st[m-j-1] = st[m-j-1], st[i+j]
		}
	}

	return string(st)
}
