
func dfs(start, node int, adj, ancestors [][]int) {
	for _, child := range adj[node] {
		if len(ancestors[child]) > 0 && ancestors[child][len(ancestors[child])-1] == start {
			continue
		}

		ancestors[child] = append(ancestors[child], start)
		dfs(start, child, adj, ancestors)
	}
}

func getAncestors(n int, edges [][]int) [][]int {
	adj := make([][]int, n)
	ancestors := make([][]int, n)

	for _, edge := range edges {
		adj[edge[0]] = append(adj[edge[0]], edge[1])
	}

	for i := 0; i < n; i++ {
		dfs(i, i, adj, ancestors)
	}

	return ancestors
}
