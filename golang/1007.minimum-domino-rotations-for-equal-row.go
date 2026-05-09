func minDominoRotations(tops []int, bottoms []int) int {
	top, bottom, all := make([]int, 7), make([]int, 7), make([]int, 7)
	n := len(tops)

	for i := range n {
		top[tops[i]]++
		bottom[bottoms[i]]++

		if tops[i] == bottoms[i] {
			all[tops[i]]++
		}
	}

	for i := 1; i <= 6; i++ {
		if top[i]+bottom[i]-all[i] == n {
			return n - max(top[i], bottom[i])
		}
	}

	return -1
}
