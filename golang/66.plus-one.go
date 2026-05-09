
func plusOne(digits []int) []int {
	var tmp int
	carry := 1

	for n := len(digits) - 1; n >= 0 && carry > 0; n-- {
		tmp = carry + digits[n]
		carry = tmp / 10
		digits[n] = tmp % 10
	}

	if carry > 0 {
		digits = append([]int{1}, digits...)
	}

	return digits
}
