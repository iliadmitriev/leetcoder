import (
	"slices"
)

func removeCoveredIntervals(intervals [][]int) int {
	slices.SortFunc(intervals, func(a, b []int) int {
		if a[0] == b[0] {
			return b[1] - a[1]
		}

		return a[0] - b[0]
	})

	count := 0
	curEnd := 0

	for _, cur := range intervals {
		if curEnd < cur[1] {
			count++
			curEnd = cur[1]
		}
	}

	return count
}