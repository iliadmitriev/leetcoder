func backspaceCompare(s string, t string) bool {
	s1, t1 := stack(s), stack(t)

	return cmp(s1, t1)
}

func stack(s string) []rune {
	stack := make([]rune, 0, len(s))
	for _, c := range s {
		if c != '#' {
			stack = append(stack, c)
		} else if len(stack) > 0 {
			stack = stack[:len(stack)-1]
		}
	}

	return stack
}

func cmp(a, b []rune) bool {
	return len(a) == len(b) && string(a) == string(b)
}
