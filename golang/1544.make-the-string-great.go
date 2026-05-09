
func makeGood(s string) string {
	st := make([]byte, 0, len(s))

	for i := range s {
		if n := len(st); n > 0 && (s[i]-st[n-1] == 32 || st[n-1]-s[i] == 32) {
			st = st[:n-1]
		} else {
			st = append(st, s[i])
		}
	}

	return string(st)
}
