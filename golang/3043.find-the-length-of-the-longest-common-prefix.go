import (
	"math"
)

func longestCommonPrefix(arr1 []int, arr2 []int) int {
	cache := make(map[int]bool, len(arr1))
	for _, num := range arr1 {
		for num > 0 {
			cache[num] = true
			num /= 10
		}
	}

	maxPrefixLen := 0

	for _, num := range arr2 {
		for num > 0 {
			if _, ok := cache[num]; ok {
				maxPrefixLen = max(maxPrefixLen, int(math.Log10(float64(num)))+1)
				break
			}
			num /= 10
		}

	}

	return maxPrefixLen
}
