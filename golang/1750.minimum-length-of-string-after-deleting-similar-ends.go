func minimumLength(s string) int {
	l, r := 0, len(s)-1
	for l < r && s[l] == s[r] {
		ch := s[l]
		for l <= r && ch == s[l] {
			l++
		}
		for l <= r && ch == s[r] {
			r--
		}
	}

	return r - l + 1
}
