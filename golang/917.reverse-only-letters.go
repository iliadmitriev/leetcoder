func reverseOnlyLetters(s string) string {
	st := []byte(s)
	i, j := 0, len(st)-1

	for i < j {
		for i < j && !isAlphabet(st[i]) {
			i++
		}
		for i < j && !isAlphabet(st[j]) {
			j--
		}

		st[i], st[j] = st[j], st[i]
		i++
		j--
	}

	return string(st)
}

func isAlphabet(b byte) bool {
	return b >= 'a' && b <= 'z' || b >= 'A' && b <= 'Z'
}
