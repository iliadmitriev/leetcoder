import "math"

func findNumbers(nums []int) int {
	total := 0

	for _, num := range nums {
		if int(math.Log10(float64(num)))%2 == 1 {
			total++
		}
	}

	return total
}
