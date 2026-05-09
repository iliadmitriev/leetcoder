func numOfUnplacedFruits(fruits []int, baskets []int) int {
	left := len(baskets)

	for _, fruit := range fruits {
		for j := range baskets {
			if fruit <= baskets[j] {
				left--
				baskets[j] = -1
				break
			}
		}
	}

	return left
}
