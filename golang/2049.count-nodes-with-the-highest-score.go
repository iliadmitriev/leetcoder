func countHighestScoreNodes(parents []int) int {
	n := len(parents)

	adj := make([][]int, len(parents))
	for i := 1; i < len(parents); i++ {
		adj[parents[i]] = append(adj[parents[i]], i)
	}

	child := make([]int, len(parents))
	child[0] = countNumChild(adj, 0, child)

	maxScore, maxCount := 0, 0
	for i := 0; i < len(parents); i++ {
		val := max(1, n-child[i])

		for _, j := range adj[i] {
			val *= child[j]
		}

		if val > maxScore {
			maxScore, maxCount = val, 1
		} else if val == maxScore {
			maxCount++
		}
	}

	return maxCount
}

func countNumChild(adj [][]int, par int, child []int) int {
	child[par] = 1
	for _, v := range adj[par] {
		child[par] += countNumChild(adj, v, child)
	}

	return child[par]
}
