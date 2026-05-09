func minSwaps(s string) int {
	stack := 0
	n := len(s)

	for i := 0; i < n; i++ {
		if s[i] == '[' {
			stack++
		} else {
			if stack > 0 {
				stack--
			}
		}
	}

	return (stack + 1) / 2
}
