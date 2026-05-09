func closestPrimes(left int, right int) []int {
	res := []int{-1, -1}
	minDiff := right - left + 1
	prev := -1

	for num := left; num <= right; num++ {
		if !checkIsPrime(num) {
			continue
		}

		if prev == -1 {
			prev = num
			continue
		}

		if num-prev <= 2 {
			return []int{prev, num}
		}

		if diff := num - prev; diff < minDiff {
			minDiff = diff
			res = []int{prev, num}
		}

		prev = num
	}

	return res
}

func checkIsPrime(num int) bool {
	if num <= 1 {
		return false
	}

	if num <= 3 {
		return true
	}

	if num%2 == 0 || num%3 == 0 {
		return false
	}

	for i := 5; i*i <= num; i += 6 {
		if num%i == 0 || num%(i+2) == 0 {
			return false
		}
	}

	return true
}
