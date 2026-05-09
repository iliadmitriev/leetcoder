
func subtractProductAndSum(n int) int {
	sum, prod := 0, 1

	for n > 0 {
		d := n % 10

		sum += d
		prod *= d

		n /= 10
	}

	return prod - sum
}
