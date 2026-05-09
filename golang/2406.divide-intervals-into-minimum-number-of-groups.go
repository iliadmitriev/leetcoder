import "sort"

func minGroups(intervals [][]int) int {
	maxGroups := 0
	n := len(intervals)

	inv := make([][2]int, 0, 2*n)
	for i := 0; i < n; i++ {
		inv = append(inv, [2]int{intervals[i][0], 1})
		inv = append(inv, [2]int{intervals[i][1] + 1, -1})
	}

	sort.Slice(inv, func(i, j int) bool {
		return inv[i][0] < inv[j][0] || inv[i][0] == inv[j][0] && inv[i][1] < inv[j][1]
	})

	currGroups := 0
	for i := 0; i < len(inv); i++ {
		currGroups += inv[i][1]
		maxGroups = max(maxGroups, currGroups)
	}

	return maxGroups
}
