func minSteps(n int) int {
	if n < 2 {
		return 0
	}

	factorSum := 0

	for n%2 == 0 {
		factorSum += 2
		n /= 2
	}

	for i := 3; i*i <= n; i += 2 {
		for n%i == 0 {
			factorSum += i
			n /= i
		}
	}

	if n > 1 {
		factorSum += n
	}

	return factorSum
}
