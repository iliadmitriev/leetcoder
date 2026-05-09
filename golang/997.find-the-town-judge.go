func findJudge(n int, trust [][]int) int {
	order := make([]int, n+1)

	for i := range trust {
		order[trust[i][0]]--
		order[trust[i][1]]++
	}

	for i := 1; i <= n; i++ {
		if order[i] == n-1 {
			return i
		}
	}

	return -1
}
