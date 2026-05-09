func removeStars(s string) string {
	st := make([]rune, 0, len(s))
	for _, ch := range s {
		if ch == '*' {
			st = st[:len(st)-1]
		} else {
			st = append(st, ch)
		}
	}

	return string(st)
}
