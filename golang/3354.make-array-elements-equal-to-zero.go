func countValidSelections(nums []int) int {
	selections := 0

	left := 0
	right := 0

	for _, num := range nums {
		right += num
	}

	for _, num := range nums {
		left += num
		right -= num

		if num != 0 {
			continue
		}

		diff := left - right
		if diff < 0 {
			diff = -diff
		}

		switch diff {
		case 0:
			selections += 2
		case 1:
			selections += 1
		}
	}

	return selections
}
