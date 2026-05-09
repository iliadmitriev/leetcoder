func highestPeak(isWater [][]int) [][]int {
	m, n := len(isWater), len(isWater[0])
	dirs := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	res := make([][]int, m)

	q := make([][2]int, 0, m*n)
	for r := 0; r < m; r++ {
		res[r] = make([]int, n)
		for c := 0; c < n; c++ {
			res[r][c] = isWater[r][c] - 1
			if res[r][c] == 0 {
				q = append(q, [2]int{r, c})
			}
		}
	}

	for len(q) > 0 {
		v := q[0]
		q = q[1:]
		r, c := v[0], v[1]

		for i := range dirs {
			nr, nc := r+dirs[i][0], c+dirs[i][1]

			if nr < 0 || nr >= m || nc < 0 || nc >= n || res[nr][nc] != -1 {
				continue
			}

			res[nr][nc] = res[r][c] + 1
			q = append(q, [2]int{nr, nc})
		}
	}

	return res
}
