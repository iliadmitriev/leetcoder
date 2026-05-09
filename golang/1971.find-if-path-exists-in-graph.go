package main

func validPath(n int, edges [][]int, source int, destination int) bool {
	adj := make([][]int, n)

	for _, edge := range edges {
		adj[edge[0]] = append(adj[edge[0]], edge[1])
		adj[edge[1]] = append(adj[edge[1]], edge[0])
	}

	visited := make([]bool, n)
	queue := make([]int, 0, n)

	queue = append(queue, source)
	visited[source] = true

	var node int
	for len(queue) > 0 {
		node, queue = queue[0], queue[1:]

		if node == destination {
			return true
		}

		for _, child := range adj[node] {
			if visited[child] {
				continue
			}

			queue = append(queue, child)
			visited[child] = true
		}
	}

	return false
}
