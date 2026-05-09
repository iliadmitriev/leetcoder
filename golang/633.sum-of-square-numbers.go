
import (
	"math"
)

func judgeSquareSum(c int) bool {
	// fermat: number can be represented as a sum of two squares if
	// all prime factors which can be expressed as 4 * k + 3
	// occurs odd

	n := int(math.Sqrt(float64(c)))

	for i := 2; i <= n; i++ {
		if c%i != 0 {
			continue
		}

		cnt := 0
		for c%i == 0 {
			cnt++
			c /= i
		}

		if i%4 == 3 && cnt%2 == 1 {
			return false
		}
	}

	return c%4 != 3
}
