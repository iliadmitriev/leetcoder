import "sort"

func minOperations(grid [][]int, x int) int {
	m, n := len(grid), len(grid[0])
	remainder := grid[0][0] % x
	buf := make([]int, m*n)
	ans, mid := 0, 0
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j]%x != remainder {
				return -1
			}

			buf[i*n+j] = grid[i][j]
		}
	}

	sort.Ints(buf)
	mid = buf[m*n/2]

	for i := 0; i < m*n; i++ {
		ans += abs(buf[i]-mid) / x
	}

	return ans
}
