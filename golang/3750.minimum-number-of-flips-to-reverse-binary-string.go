import (
	"math/bits"
)

func minimumFlips(n int) int {
	w := 64 - bits.LeadingZeros(uint(n)) // integer bit width
	count := 0

	for x, i := n, w-1; x > 0; x, i = x>>1, i-1 {
		s := x & 1        // iterate right to left
		r := (n >> i) & 1 // iterate left to right

		if r != s {
			count++
		}
	}

	return count
}