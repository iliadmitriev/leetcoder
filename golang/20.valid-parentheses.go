func isValid(s string) bool {
	st := []byte{}

	tb := map[byte]byte{
		'(': ')',
		'[': ']',
		'{': '}',
	}

	for i := range len(s) {
		c := s[i]

		if _, ok := tb[c]; ok {
			st = append(st, c)
		} else if len(st) == 0 || tb[st[len(st)-1]] != c {
			return false
		} else {
			st = st[:len(st)-1]
		}
	}

	return len(st) == 0
}