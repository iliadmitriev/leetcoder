import (
	"slices"
	"cmp"
)

func lexicographicallySmallestArray(nums []int, limit int) []int {
	n := len(nums)
	res := make([]int, n)

	// sorted slice of pairs {{value, position}, ...}
	data := make([][2]int, n)
	for i, v := range nums {
		data[i] = [2]int{v, i}
	}
	slices.SortFunc(data, func(a, b [2]int) int {
		return cmp.Compare(a[0], b[0])
	})

	values := make([]int, 0, n)
	values = append(values, data[0][0])

	positions := make([]int, 0, n)
	positions = append(positions, data[0][1])

	drain := func(res, values, positions []int) {
		slices.Sort(positions) // sort positions (values already sorted)

		for k, j := range positions {
			res[j] = values[k]
		}
	}

	for i := 1; i < n; i++ {
		if data[i][0]-data[i-1][0] > limit {
			drain(res, values, positions)
			values = values[:0]
			positions = positions[:0]
		}

		values = append(values, data[i][0])
		positions = append(positions, data[i][1])
	}

	drain(res, values, positions)

	return res
}