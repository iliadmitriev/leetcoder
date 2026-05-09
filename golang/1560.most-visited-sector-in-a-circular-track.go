func mostVisited(n int, rounds []int) []int {
	start, end := rounds[0], rounds[len(rounds)-1]

	res := ([]int)(nil)

	if start > end {
		res = make([]int, 0, n-start+end+1)

		for i := 1; i <= end; i++ {
			res = append(res, i)
		}

		for i := start; i <= n; i++ {
			res = append(res, i)
		}

	} else {

		res = make([]int, 0, end-start+1)
		for i := start; i <= end; i++ {
			res = append(res, i)
		}
	}

	return res
}
