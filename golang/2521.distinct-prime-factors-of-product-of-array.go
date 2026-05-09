func distinctPrimeFactors(nums []int) int {
	n := len(nums)
	cache := make(map[int]bool, min(1001, n))
	primes := make(map[int]bool, min(1001, n))

	for _, num := range nums {
		if cache[num] {
			continue
		}

		cache[num] = true

		for num%2 == 0 {
			num /= 2
			primes[2] = true
		}

		for d := 3; d*d <= num; d += 2 {
			for num%d == 0 {
				num /= d
				primes[d] = true
			}
		}

		if num > 1 {
			primes[num] = true
		}

	}

	return len(primes)
}
