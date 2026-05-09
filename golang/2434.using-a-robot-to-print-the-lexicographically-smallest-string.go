func robotWithString(s string) string {
	n := len(s)
	cnt := make([]int, 26)
	res := make([]byte, 0, n)
	st := make([]byte, 0, n/4)

	for _, c := range s {
		cnt[c-'a']++
	}

	i := 0

	for c := byte('a'); c <= 'z'; c++ {
		// pop from stack all the characters that are less than or equal to current character
		for len(st) > 0 && st[len(st)-1] <= c {
			res = append(res, st[len(st)-1])
			st = st[:len(st)-1]
		}

		for cnt[c-'a'] > 0 {
			if s[i] == c {
				res = append(res, s[i])
			} else {
				st = append(st, s[i])
			}

			cnt[s[i]-'a']--
			i++
		}
	}

	for len(st) > 0 {
		res = append(res, st[len(st)-1])
		st = st[:len(st)-1]
	}

	return string(res)
}
