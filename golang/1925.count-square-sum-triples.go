
import "math"

func countTriples(n int) int {
	count := 0

	for i := 1; i <= n; i++ {
		for j := i; j <= n; j++ {
			v := i*i + j*j
			r := int(math.Sqrt(float64(v)))

			if r > n {
				break
			}

			if r*r == v {
				count++
			}
		}
	}

	return count * 2
}
