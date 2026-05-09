func reverseParentheses(s string) string {
	cur := make([]rune, 0, len(s))
	st := make([]int, 0, len(s)/2)

	for _, r := range s {
		if r == '(' {
			st = append(st, len(cur))
		} else if r == ')' {
			reverseRuneArr(cur, st[len(st)-1])
			st = st[:len(st)-1]
		} else {
			cur = append(cur, r)
		}
	}

	return string(cur)
}

func reverseRuneArr(r []rune, i int) {
	for j := len(r) - 1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
}
