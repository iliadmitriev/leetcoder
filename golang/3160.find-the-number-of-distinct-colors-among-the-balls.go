func queryResults(limit int, queries [][]int) []int {
	N := len(queries)
	colors := make(map[int]int)
	balls := make(map[int]int)
	res := make([]int, N)

	for i := 0; i < N; i++ {
		ball, color := queries[i][0], queries[i][1]

		prevColor := balls[ball]
		balls[ball] = color

		colors[color]++
		if prevColor > 0 {
			colors[prevColor]--

			if colors[prevColor] == 0 {
				delete(colors, prevColor)
			}
		}

		res[i] = len(colors)
	}

	return res
}
