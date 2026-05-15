func separateDigits(nums []int) []int {
	n := len(nums)
	res := make([]int, 0, n)
	digits := make([]int, 0, 6)

	for _, num := range nums {
		for num > 0 {
			digits = append(digits, num%10)
			num /= 10
		}

		for len(digits) > 0 {
			res = append(res, digits[len(digits) - 1])
			digits = digits[:len(digits)-1]
		}
	}

	return res
}