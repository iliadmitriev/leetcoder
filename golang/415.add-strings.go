func addStrings(num1 string, num2 string) string {
	l1, l2 := len(num1), len(num2)
	t := max(l1, l2)
	x, y := byte(0), byte(0)
	carry := byte(0)
	res := make([]byte, 0, t+1)

	for i := range t {
		x = 0
		if i < l1 {
			x = num1[l1-i-1] - '0'
		}

		y = 0
		if i < l2 {
			y = num2[l2-i-1] - '0'
		}

		sum := x + y + carry
		carry = sum / 10
		sum = sum % 10

		res = append(res, sum+'0')

	}

	if carry > 0 {
		res = append(res, carry+'0')
	}

	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}

	return string(res)
}
