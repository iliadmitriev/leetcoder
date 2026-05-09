func punishmentNumber(n int) int {
	total := 0

	for num := 1; num <= n; num++ {
		value := num * num

		if isPunishmentNumber(value, num) {
			total += value
		}
	}

	return total
}

func isPunishmentNumber(num, target int) bool {
	if num == 0 && target == 0 {
		return true
	}

	if num == 0 || target < 0 {
		return false
	}

	place := 1
	for num/place > 0 {
		place *= 10

		if isPunishmentNumber(num/place, target-num%place) {
			return true
		}
	}

	return false
}
