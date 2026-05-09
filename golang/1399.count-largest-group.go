func countLargestGroup(n int) int {
	limit := sumDigits(10000-1) + 1
	counter := make([]int, limit)
	largest, largestCount := 0, 0

	for i := 1; i <= n; i++ {
		counter[sumDigits(i)]++
	}

	for _, v := range counter {
		if v > largest {
			largest = v
			largestCount = 1
		} else if v == largest {
			largestCount++
		}
	}

	return largestCount
}

func sumDigits(num int) int {
	res := 0
	for num > 0 {
		res += num % 10
		num /= 10
	}

	return res
}
