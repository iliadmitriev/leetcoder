func hasGroupsSizeX(deck []int) bool {
	cache := make(map[int]int, len(deck))

	for _, v := range deck {
		cache[v]++
	}

	divisor := cache[deck[0]]
	for _, v := range cache {

		divisor = gcdEuclid(v, divisor)

		if divisor == 1 {
			return false
		}
	}

	for _, v := range cache {
		if v%divisor != 0 {
			return false
		}
	}

	return true
}

func gcdEuclid(a, b int) int {
	for b > 0 {
		a, b = b, a%b
	}

	return a
}
