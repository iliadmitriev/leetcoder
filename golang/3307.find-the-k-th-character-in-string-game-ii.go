import (
	"math/bits"
)

func kthCharacter(k int64, operations []int) byte {
	res := 0
	n := uint64(k - 1)

	for n > 0 {
		// t - bits length of n - 1
		t := bits.Len64(n) - 1
		n -= 1 << t

		res += operations[t]
	}

	return byte('a' + res%26)
}
