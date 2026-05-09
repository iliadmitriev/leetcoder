
func reverseString(s string) string {
	tmp := []rune(s)
	n := len(tmp)

	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		tmp[i], tmp[j] = tmp[j], tmp[i]
	}

	return string(tmp)
}

func isSubstringPresent(s string) bool {
	r := make(map[string]bool, len(s))
	rev := reverseString(s)

	for i := 0; i < len(rev)-1; i++ {
		r[rev[i:i+2]] = true
	}

	for i := 0; i < len(s)-1; i++ {
		if _, ok := r[s[i:i+2]]; ok {
			return true
		}
	}

	return false
}
