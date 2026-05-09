
func insert(intervals [][]int, newInterval []int) [][]int {
	res := make([][]int, 0, len(intervals)+1)

	for _, intv := range intervals {
		if intv[1] < newInterval[0] {
			res = append(res, intv)
		} else if intv[0] > newInterval[1] {
			res = append(res, newInterval)
			newInterval = intv
		} else {
			newInterval[0] = min(intv[0], newInterval[0])
			newInterval[1] = max(intv[1], newInterval[1])
		}
	}

	res = append(res, newInterval)

	return res
}
