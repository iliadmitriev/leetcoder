func isPrimeNum(n int) bool {
	if n < 2 {
		return false
	}

	if n < 4 {
		return true
	}

	if n%2 == 0 {
		return false
	}

	for i := 3; i*i <= n; i += 2 {
		if n%i == 0 {
			return false
		}
	}

	return true
}

func numPrimeArrangements(n int) int {
	primes, notPrimes := 0, n

	for i := 1; i <= n; i++ {
		if isPrimeNum(i) {
			primes++
		}
	}

	notPrimes -= primes

	total := 1
	const MOD = int(1e9) + 7

	for i := 2; i <= primes; i++ {
		total *= i
		total %= MOD
	}

	for i := 2; i <= notPrimes; i++ {
		total *= i
		total %= MOD
	}

	return total
}
