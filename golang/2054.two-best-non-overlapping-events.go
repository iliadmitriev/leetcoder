import (
	"sort"
)

func maxTwoEvents(events [][]int) int {
	n := len(events)
	sort.Slice(events, func(i, j int) bool {
		return events[i][1] < events[j][1]
	})

	// tuples of (weight, end idx)
	prefixMax := make([][2]int, 0, n+1)
	prefixMax = append(prefixMax, [2]int{0, -1})

	maxTwo := 0

	for _, event := range events {
		start, end, weight := event[0], event[1], event[2]

		idx := prevMaxEventIdx(prefixMax, start-1) - 1

		maxTwo = max(maxTwo, prefixMax[idx][0]+weight)

		if weight > prefixMax[len(prefixMax)-1][0] {
			prefixMax = append(prefixMax, [2]int{weight, end})
		}
	}

	return maxTwo
}

func prevMaxEventIdx(prefix [][2]int, x int) int {
	lo, hi := 0, len(prefix)
	var mid int

	for lo < hi {
		mid = (lo + hi) / 2
		if x < prefix[mid][1] {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}
