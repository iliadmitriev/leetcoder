import (
	"slices"
)

func findMissingElements(nums []int) []int {
	start := slices.Min(nums)
	end := slices.Max(nums)

	cache := make(map[int]struct{})
	for _, v := range nums {
		cache[v] = struct{}{}
	}

	res := make([]int, 0, end-start+1-len(cache))

	for v := start; v < end; v++ {
		if _, ok := cache[v]; !ok {
			res = append(res, v)
		}
	}

	return res
}