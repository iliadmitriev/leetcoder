func minRemoveToMakeValid(s string) string {
	tmp := []byte(s)
	stack := make([]int, 0, len(s)/2)

	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack = append(stack, i)
		} else if s[i] == ')' {
			if len(stack) > 0 && s[stack[len(stack)-1]] == '(' {
				stack = stack[:len(stack)-1]
			} else {
				stack = append(stack, i)
			}
		}
	}

	for len(stack) > 0 {
		tmp[stack[len(stack)-1]] = 0
		stack = stack[:len(stack)-1]
	}

	res := make([]byte, 0, len(s))
	for i := 0; i < len(tmp); i++ {
		if tmp[i] != 0 {
			res = append(res, tmp[i])
		}
	}

	return string(res)
}
