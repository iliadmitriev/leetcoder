
func maxSumDivThree(nums []int) int {
	total := 0
	for _, num := range nums {
		total += num
	}

	rem := total % 3
	if rem == 0 {
		return total
	}

	const INF = int(1e9)
	a1, b1 := INF, INF // two smallest numbers with remainder 1
	a2, b2 := INF, INF // two smallest numbers with remainder 2

	for _, num := range nums {
		switch num % 3 {
		case 1:
			if num <= a1 {
				b1 = a1
				a1 = num
			} else if num < b1 {
				b1 = num
			}
		case 2:
			if num <= a2 {
				b2 = a2
				a2 = num
			} else if num < b2 {
				b2 = num
			}
		}
	}

	if rem == 1 {
		return total - min(a1, a2+b2)
	} else { // rem == 2
		return total - min(a1+b1, a2)
	}
}
