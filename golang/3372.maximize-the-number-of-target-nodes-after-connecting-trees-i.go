func maxTargetNodes(edges1 [][]int, edges2 [][]int, k int) []int {
	adj1 := buildAdjTree(edges1)

	if k < 2 {
		res := make([]int, len(adj1))
		for i := range res {
			res[i] = dfsDepthCount(adj1, i, -1, k) + k
		}
		return res
	}

	adj2 := buildAdjTree(edges2)
	max2 := 0

	for i := range adj2 {
		max2 = max(max2, dfsDepthCount(adj2, i, -1, k-1))
	}

	res := make([]int, len(adj1))
	for i := range res {
		res[i] = dfsDepthCount(adj1, i, -1, k) + max2
	}
	return res
}

func dfsDepthCount(adj [][]int, node, parent, depth int) int {
	if depth < 0 {
		return 0
	}
	count := 1
	for _, child := range adj[node] {
		if child == parent {
			continue
		}
		count += dfsDepthCount(adj, child, node, depth-1)
	}
	return count
}

func buildAdjTree(edges [][]int) [][]int {
	adj := make([][]int, len(edges)+1)
	for _, edge := range edges {
		adj[edge[0]] = append(adj[edge[0]], edge[1])
		adj[edge[1]] = append(adj[edge[1]], edge[0])
	}
	return adj
}
