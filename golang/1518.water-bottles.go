func numWaterBottles(numBottles int, numExchange int) int {
	empty, total := 0, 0

	for numBottles > 0 {
		empty += numBottles
		total += numBottles
		numBottles = empty / numExchange
		empty %= numExchange
	}

	return total
}
