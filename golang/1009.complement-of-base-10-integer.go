import (
	"math/bits"
)

func bitwiseComplement(n int) int {
	bitLen := func(n int) int {
		return 32 - bits.LeadingZeros32(uint32(n))
	}

	mask := (1 << bitLen(max(1, n))) - 1

	return mask ^ n
}