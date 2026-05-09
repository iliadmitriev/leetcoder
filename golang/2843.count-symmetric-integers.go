
func countSymmetricIntegers(low int, high int) int {
	res := 0
	for i := low; i <= high; i++ {
		res += symmetricInteger(i)
	}
	return res
}

func symmetricInteger(x int) int {
	div := 0
	if 10 <= x && x <= 99 {
		div = 10
	} else if 1000 <= x && x <= 9999 {
		div = 100
	} else {
		return 0
	}

	left, right := x/div, x%div

	if sumDigits(left) == sumDigits(right) {
		return 1
	}

	return 0
}

func sumDigits(x int) int {
	res := 0
	for x > 0 {
		res += x % 10
		x /= 10
	}
	return res
}
