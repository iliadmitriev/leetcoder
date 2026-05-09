func selfDividingNumbers(left int, right int) []int {
	arr := make([]int, 0)

	isSelfDivisible := func(num int) bool {
		tmp := num

		for tmp > 0 {
			digit := tmp % 10
			tmp /= 10

			if digit == 0 || num%digit != 0 {
				return false
			}
		}

		return true
	}

	for i := left; i <= right; i++ {
		if isSelfDivisible(i) {
			arr = append(arr, i)
		}
	}

	return arr
}
