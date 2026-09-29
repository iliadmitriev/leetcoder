func hasValidPath(grid [][]byte) bool {

	m, n := len(grid), len(grid[0])
	pathLen := m + n - 1

	if pathLen%2 == 1 || grid[0][0] == ')' || grid[m-1][n-1] == '(' {
		return false
	}

	memo := make([][][]int, m)
	for i := range m {
		memo[i] = make([][]int, n)
		for j := range n {
			memo[i][j] = make([]int, pathLen+1) // can't exceed m + n
			for k := range pathLen + 1 {
				memo[i][j][k] = -1 // unvisited
			}
		}
	}

	var dfs func(int, int, int) bool
	dfs = func(i, j, cnt int) bool {
		if i == m || j == n {
			return false
		}

		if grid[i][j] == '(' {
			cnt++
		} else if grid[i][j] == ')' {
			cnt--
		}

		if cnt < 0 || cnt > (m-1-i)+(n-1-j) {
			return false
		}

		if i == m-1 && j == n-1 {
			return cnt == 0
		}

		if memo[i][j][cnt] != -1 {
			return memo[i][j][cnt] == 1
		}

		res := dfs(i+1, j, cnt) || dfs(i, j+1, cnt)
		if res {
			memo[i][j][cnt] = 1
		} else {
			memo[i][j][cnt] = 0
		}

		return res
	}

	return dfs(0, 0, 0)
}