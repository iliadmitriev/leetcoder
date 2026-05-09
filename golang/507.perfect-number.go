func checkPerfectNumber(num int) bool {
	if num == 1 {
		return false
	}

	s := 1 // total sum of all positive divisors
	for i := 2; i*i <= num; i += 2 {
		if num%i == 0 {
			s += i
			s += num / i
		}
	}

	return s == num
}
