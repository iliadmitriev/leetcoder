import (
	"math"
)

func reorderedPowerOf2(n int) bool {
	m := min(int(1e9), int(math.Pow10(int(math.Ceil(math.Log10(float64(n+1)))))))
	f := countDigits(n)

	for x := 1; x <= m; x <<= 1 {
		if f == countDigits(x) {
			return true
		}
	}

	return false
}

func countDigits(x int) [10]int {
	res := [10]int{}
	for x > 0 {
		res[x%10]++
		x /= 10
	}

	return res
}
