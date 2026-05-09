func maxBottlesDrunk(numBottles int, numExchange int) int {
	empty := numBottles

	for empty >= numExchange {
		empty -= numExchange
		empty++
		numBottles++
		numExchange++
	}

	return numBottles
}
