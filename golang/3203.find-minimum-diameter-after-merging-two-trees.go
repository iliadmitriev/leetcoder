func minimumDiameterAfterMerge(edges1 [][]int, edges2 [][]int) int {
	adj1, adj2 := buildAdjTree(edges1), buildAdjTree(edges2)

	d1, _ := getTreeDiameterPath(0, -1, adj1)
	d2, _ := getTreeDiameterPath(0, -1, adj2)

	return max(
		max(d1, d2),
		1+(d1/2+d1%2)+(d2/2+d2%2),
	)
}

func getTreeDiameterPath(node, parent int, edges [][]int) (int, int) {
	maxDia, maxPath1, maxPath2 := 0, 0, 0

	for _, child := range edges[node] {
		if child == parent {
			continue
		}

		childDia, childPath := getTreeDiameterPath(child, node, edges)
		maxDia = max(maxDia, childDia)

		if childPath >= maxPath1 {
			maxPath2 = maxPath1
			maxPath1 = childPath
		} else if childPath > maxPath2 {
			maxPath2 = childPath
		}

	}

	maxDia = max(maxDia, maxPath1+maxPath2)

	return maxDia, 1 + max(maxPath1, maxPath2)
}

func buildAdjTree(edges [][]int) [][]int {
	k := len(edges)
	adj := make([][]int, k+1)

	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], e[1])
		adj[e[1]] = append(adj[e[1]], e[0])
	}

	return adj
}
