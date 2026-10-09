func minInsertions(s string) int {
	closingNeeded := 0
	res := 0

	for _, ch := range s {
		switch ch {
		case '(':
			{
				closingNeeded += 2

				if closingNeeded%2 == 1 {
					closingNeeded--
					res++
				}
			}
		case ')':
			{
				closingNeeded -= 1

				if closingNeeded < 0 {
					res++
					closingNeeded += 2
				}
			}
		}
	}

	return res + closingNeeded
}