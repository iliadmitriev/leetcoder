
const MOD = int(1e9) + 7

func getFactorsCount(limit int) [][]int {
	factors := make([][]int, limit+1)
	primes := make([]int, limit+1)

	for i := 2; i <= limit; i++ {
		if primes[i] != 0 {
			continue
		}

		for j := i; j <= limit; j += i {
			if primes[j] != 0 {
				continue
			}
			primes[j] = i
		}
	}

	for i := 2; i <= limit; i++ {
		num := i
		p := primes[i]
		d := make(map[int]int)

		for num > 1 {
			d[p]++
			num /= p
			p = primes[num]
		}

		factors[i] = make([]int, 0, len(d))
		for _, v := range d {
			factors[i] = append(factors[i], v)
		}
	}

	return factors
}

func getCombinations(n, k, mod int) int {
	if n < k {
		return 0
	}

	r := 1
	for i := range k {
		r *= (n - i)
		r %= mod
		r *= expMod(i+1, -1, mod)
		r %= mod
	}

	return r
}

func idealArrays(n int, maxValue int) int {
	total := 0

	factors := getFactorsCount(maxValue)

	for i := 1; i <= maxValue; i++ {

		prod := 1
		for _, v := range factors[i] {
			prod *= getCombinations(n-1+v, v, MOD)
			prod %= MOD
		}

		total += prod
		total %= MOD
	}

	return total
}

// expMod modular exponentiation, with possible negative exponent
func expMod(base, exp, mod int) int {
	if exp < 0 {
		inverse := getInverse(base, mod)
		return expMod(inverse, -exp, mod)
	}
	res := 1
	base %= mod

	for exp > 0 {
		if exp&1 == 1 {
			res *= base
			res %= mod
		}
		base *= base
		base %= mod
		exp >>= 1
	}

	return res
}

// getInverse returns the inverse of a based on Euclidean algorithm
func getInverse(a, mod int) int {
	g, x, _ := getGCD(a, mod)

	if g != 1 {
		panic("modular inverse does not exist")
	}

	return (x%mod + mod) % mod
}

// getGCD returns the greatest common divisor of a and b, extended Euclidean algorithm
func getGCD(a, b int) (int, int, int) {
	if b == 0 {
		return a, 1, 0
	}
	g, x, y := getGCD(b, a%b)
	return g, y, x - (a/b)*y
}
