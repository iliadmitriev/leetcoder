func eventualSafeNodes(graph [][]int) []int {
	N := len(graph)
	revGraph := make([][]int, N)
	outDegree := make([]int, N)
	safeNodes := make([]bool, N)
	safe := make([]int, 0)
	que := make([]int, 0, N)

	for i := 0; i < N; i++ {
		for _, j := range graph[i] {
			revGraph[j] = append(revGraph[j], i)
			outDegree[i]++
		}

		if len(graph[i]) == 0 {
			que = append(que, i)
		}
	}

	for len(que) > 0 {
		node := que[0]
		que = que[1:]
		safeNodes[node] = true

		for _, nNode := range revGraph[node] {
			outDegree[nNode]--
			if outDegree[nNode] == 0 {
				que = append(que, nNode)
			}
		}
	}

	for i := 0; i < N; i++ {
		if safeNodes[i] {
			safe = append(safe, i)
		}
	}

	return safe
}
