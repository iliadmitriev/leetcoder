
func minAddToMakeValid(s string) int {
	n := len(s)
	closed, opened := 0, 0

	for i := 0; i < n; i++ {
		if s[i] == '(' {
			opened++
		} else if opened > 0 && s[i] == ')' {
			opened--
		} else if s[i] == ')' {
			closed++
		}
	}

	return closed + opened
}
