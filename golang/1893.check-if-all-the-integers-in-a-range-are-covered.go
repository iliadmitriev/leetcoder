func isCovered(ranges [][]int, left int, right int) bool {

	cover := make([]int, 52)
	for _, r := range ranges {
		cover[r[0]]++
		cover[r[1]+1]--
	}

	coverage := 0

	for i := 1; i <= right; i++ {
		coverage += cover[i]

		if left <= i && coverage == 0 {
			return false
		}
	}

	return true
}
