func numSteps(s string) int {
	moves := 0
	carry, digit := 0, 0

	for i := len(s) - 1; i > 0; i-- {
		digit = int(s[i]-'0') + carry
		moves += 1 + (digit % 2)
		carry = (1 + digit) / 2
	}

	return moves + carry
}
