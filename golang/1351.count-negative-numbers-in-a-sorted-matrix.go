
func zeroPos(arr []int, lo, hi int) int {
	// var mid int
	//
	// for lo < hi {
	// 	mid = (lo + hi) / 2
	// 	if arr[mid] >= 0 {
	// 		lo = mid + 1
	// 	} else {
	// 		hi = mid
	// 	}
	// }
	//
	// return lo

	for i := hi; i > lo; i-- {
		if arr[i-1] >= 0 {
			return i
		}
	}

	return 0
}

func countNegatives(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	count := 0
	cur := n

	for i := range m {

		cur = zeroPos(grid[i], 0, cur)

		count += n - cur
	}

	return count
}
