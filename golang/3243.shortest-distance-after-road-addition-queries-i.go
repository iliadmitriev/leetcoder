func shortestDistanceAfterQueries(n int, queries [][]int) []int {
	adj := make([][]int, n)
	for i := 1; i < n; i++ {
		adj[i-1] = append(adj[i-1], i)
	}

	m := len(queries)
	answer := make([]int, m)

	dist := make([]int, n)
	for i := range dist {
		dist[i] = i
	}

	for i := 0; i < m; i++ {
		u, v := queries[i][0], queries[i][1]
		adj[u] = append(adj[u], v)

		if dist[v] > dist[u]+1 {
			bfsShortestPath(adj, dist, u)
		}

		answer[i] = dist[n-1]
	}

	return answer
}

func bfsShortestPath(adj [][]int, dist []int, start int) {
	n := len(dist)
	q := make([]int, 0, n-start+1)

	q = append(q, start)

	for step := 0; len(q) > 0; step++ {
		cur := q[0]
		q = q[1:]

		if cur == n-1 {
			return
		}

		for _, child := range adj[cur] {
			if dist[child] <= dist[cur]+1 {
				continue
			}

			q = append(q, child)
			dist[child] = dist[cur] + 1

		}
	}
}
