func differenceOfSums(n int, m int) int {
	num1 := n * (n + 1) / 2
	k := n / m
	num2 := k * (k + 1) / 2 * m

	return num1 - 2*num2
}
