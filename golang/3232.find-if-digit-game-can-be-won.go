func canAliceWin(nums []int) bool {
	single, double := 0, 0

	for _, num := range nums {
		if num < 10 {
			single += num
		} else {
			double += num
		}
	}

	return single < double || single > double
}
