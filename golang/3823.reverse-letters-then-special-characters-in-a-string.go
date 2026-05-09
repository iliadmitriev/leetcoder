func reverseByType(s string) string {
	n := len(s)
	buf := []byte(s)

	solve := func(cond func(byte) bool) {
		for i, j := 0, n-1; i < j; {
			if !cond(buf[i]) {
				i++
				continue
			}

			if !cond(buf[j]) {
				j--
				continue
			}

			buf[i], buf[j] = buf[j], buf[i]
			i, j = i+1, j-1
		}
	}

	solve(func(c byte) bool {
		return 'a' <= c && c <= 'z'
	})

	solve(func(c byte) bool {
		return 'a' > c || c > 'z'
	})

	return string(buf)
}