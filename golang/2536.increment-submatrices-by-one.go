
func rangeAddQueries(n int, queries [][]int) [][]int {
	prefix := make([][]int, n+1)

	for i := range n + 1 {
		prefix[i] = make([]int, n+1)
	}

	for _, q := range queries {
		y1, x1, y2, x2 := q[0], q[1], q[2], q[3]
		prefix[y1][x1]++     // top left
		prefix[y1][x2+1]--   // top right
		prefix[y2+1][x1]--   // bottom left
		prefix[y2+1][x2+1]++ // bottom right
	}

	res := make([][]int, n)
	for i := range n {
		res[i] = make([]int, n)
	}

	for i := range n {
		row := 0
		for j := range n {
			row += prefix[i][j]
			res[i][j] = row

			if i == 0 {
				continue
			}

			res[i][j] += res[i-1][j]
		}
	}

	return res
}
