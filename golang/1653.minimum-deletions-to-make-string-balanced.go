func minimumDeletions(s string) int {
	n := len(s)
	suf := 0

	for i := 0; i < n; i++ {
		if s[i] == 'a' {
			suf++
		}
	}

	res := n
	pref := 0
	for i := 0; i < n; i++ {
		if s[i] == 'a' {
			suf--
		}

		res = min(res, pref+suf)

		if s[i] == 'b' {
			pref++
		}
	}

	return res
}
