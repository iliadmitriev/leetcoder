
func digitSum(num int) int {
	s := 0
	for num > 0 {
		s += num % 10
		num /= 10
	}

	return s
}

func differenceOfSum(nums []int) int {
	total, totalDigit := 0, 0
	for _, num := range nums {
		total += num
		totalDigit += digitSum(num)
	}

	if total > totalDigit {
		return total - totalDigit
	}

	return totalDigit - total
}
