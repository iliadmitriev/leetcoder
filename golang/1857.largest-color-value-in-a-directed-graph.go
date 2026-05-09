func largestPathValue(colors string, edges [][]int) int {
	n := len(colors)
	visited := 0
	maxColors := 0
	invAdj := make([][]int, n)
	inDegree := make([]int, n)
	q := make([]int, 0, n)
	colorCount := make([]map[byte]int, n)

	for i := range n {
		colorCount[i] = make(map[byte]int)
	}

	for _, edge := range edges {
		invAdj[edge[1]] = append(invAdj[edge[1]], edge[0])
		inDegree[edge[0]]++
	}

	for i := range n {
		if inDegree[i] == 0 {
			q = append(q, i)
		}
	}

	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		visited++
		colorCount[node][colors[node]]++
		maxColors = max(maxColors, colorCount[node][colors[node]])

		for _, child := range invAdj[node] {
			for color, count := range colorCount[node] {
				colorCount[child][color] = max(colorCount[child][color], count)
			}

			inDegree[child]--
			if inDegree[child] == 0 {
				q = append(q, child)
			}
		}
	}

	if visited < n {
		return -1
	}

	return maxColors
}
