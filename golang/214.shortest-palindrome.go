func shortestPalindrome(s string) string {
	if len(s) == 0 {
		return s
	}

	prefix, suffix := 0, 0
	power := 1
	const base = 26
	const mod = int(1e9) + 7
	n := len(s)
	st := make([]int, 0)

	for i := 0; i < n; i++ {
		ch := int(s[i] - 'a' + 1)

		prefix = (prefix * base) % mod
		prefix = (prefix + ch) % mod

		suffix = (suffix + ch*power) % mod
		power = (power * base) % mod

		if suffix == prefix {
			st = append(st, i)
		}
	}

	for len(st) > 0 {
		i := st[len(st)-1]
		st = st[:len(st)-1]

		if _isPalindrome(s, 0, i) {
			rev := _reverseString(s[i+1:])
			return rev + s
		}
	}

	rev := _reverseString(s[1:])
	return rev + s
}

func _isPalindrome(s string, i, j int) bool {
	for i < j {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}

func _reverseString(s string) string {
	n := len(s)
	res := []byte(s)
	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return string(res)
}
