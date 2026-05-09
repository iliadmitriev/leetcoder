func maxDepth(s string) int {
	stack := []int{}
	res := 0

	for _, c := range s {
		if c == '(' {
			stack = append(stack, 0)
		} else if c == ')' {
			stack = stack[:len(stack)-1]
		}
		if res < len(stack) {
			res = len(stack)
		}
	}

	return res
}
