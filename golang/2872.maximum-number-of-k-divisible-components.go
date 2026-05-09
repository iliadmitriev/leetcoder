func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	maxComp, _ := dfsKDivComp(0, -1, k, adj, values)
	return maxComp
}

func dfsKDivComp(node, parent, k int, adj [][]int, values []int) (int, int) {
	total := values[node]
	maxComp := 0

	for _, child := range adj[node] {
		if child == parent {
			continue
		}

		comp, add := dfsKDivComp(child, node, k, adj, values)
		total += add
		maxComp += comp

	}

	if total%k == 0 {
		return maxComp + 1, total
	}

	return maxComp, total
}
