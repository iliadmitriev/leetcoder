import (
	"math/bits"
)

func countMonobit(n int) int {
	w := 64 - bits.LeadingZeros64(uint64(n))
	if n&(n+1) == 0 { // if rightmost number of interval consist only from 1's
		w++ // include it to result
	}

	return w
}