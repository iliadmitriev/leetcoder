func maxDepthAfterSplit(seq string) []int {
	depth := 0
	res := make([]int, len(seq))

	for i, ch := range seq {
		switch ch {
		case '(':
			{
				depth = 1 - depth
				res[i] = depth
			}
		case ')':
			{
				res[i] = depth
				depth = 1 - depth
			}
		}
	}

	return res
}