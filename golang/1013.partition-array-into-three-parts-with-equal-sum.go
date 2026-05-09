func canThreePartsEqualSum(arr []int) bool {
	total := 0
	for _, v := range arr {
		total += v
	}

	if total%3 != 0 {
		return false
	}

	partial := total / 3
	sum := 0
	state := 0

	for _, v := range arr {
		sum += v
		if sum == partial {
			state++
			sum = 0
		}

		if state == 3 {
			return true
		}
	}

	return false
}
