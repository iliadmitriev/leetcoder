func minAbsDiff(grid [][]int, k int) [][]int {
	m, n := len(grid), len(grid[0])
	ans := make([][]int, m-k+1)
	for i := range m - k + 1 {
		ans[i] = make([]int, n-k+1)
	}

	if k == 1 {
		return ans
	}

	// abs := func (x int) int {
	//   if x < 0 {
	//     return -x
	//   }
	//   return x
	// }

	for i := range m - k + 1 {
		for j := range n - k + 1 {

			sub := make([]int, 0, k*k)

			for di := range k {
				for dj := range k {
					sub = append(sub, grid[i+di][j+dj])
				}
			}

			sort.Ints(sub)

			diff := sub[k*k-1] - sub[0]
			for t := range k*k - 1 {
				if sub[t+1]-sub[t] > 0 {
					diff = min(diff, sub[t+1]-sub[t])
				}
			}

			ans[i][j] = diff
		}
	}

	return ans
}