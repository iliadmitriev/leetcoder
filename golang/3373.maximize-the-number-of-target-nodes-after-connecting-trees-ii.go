func maxTargetNodes(edges1 [][]int, edges2 [][]int) []int {
	adj1 := buildAdjList(edges1)
	adj2 := buildAdjList(edges2)

	n, m := len(adj1), len(adj2)

	even1 := dfsCountEvenNodes(adj1, 0, -1, 0)
	even2 := dfsCountEvenNodes(adj2, 0, -1, 0)

	odd1, odd2 := n-even1, m-even2

	max2 := max(even2, odd2)
	counts1 := []int{even1 + max2, odd1 + max2}

	res := make([]int, n)

	dfsSetNodesCounts(adj1, 0, -1, 0, counts1, res)
	return res
}

func buildAdjList(edges [][]int) [][]int {
	adj := make([][]int, len(edges)+1)
	for _, edge := range edges {
		adj[edge[0]] = append(adj[edge[0]], edge[1])
		adj[edge[1]] = append(adj[edge[1]], edge[0])
	}
	return adj
}

func dfsCountEvenNodes(adj [][]int, node, parent int, even int) int {
	count := 0

	if even == 0 {
		count++
	}

	for _, child := range adj[node] {
		if child == parent {
			continue
		}
		count += dfsCountEvenNodes(adj, child, node, even^1)
	}
	return count
}

func dfsSetNodesCounts(adj [][]int, node, parent int, even int, counts []int, nodes []int) {
	nodes[node] = counts[even]

	for _, child := range adj[node] {
		if child == parent {
			continue
		}
		dfsSetNodesCounts(adj, child, node, even^1, counts, nodes)
	}
}
