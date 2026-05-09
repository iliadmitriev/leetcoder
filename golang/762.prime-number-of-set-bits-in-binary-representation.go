import (
	"math/bits"
)

func countPrimeSetBits(left int, right int) int {
	primes := []int{
		2, 3, 5, 7, 11, 13, 17, 19,
	}

	mask := 0
	for _, p := range primes {
		mask |= 1 << p
	}

	counter := 0
	bound := uint(right) + 1

	for n := uint(left); n < bound; n++ {
		if (1<<bits.OnesCount(n))&mask > 0 {
			counter++
		}
	}

	return counter
}