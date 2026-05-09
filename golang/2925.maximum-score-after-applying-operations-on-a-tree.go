func dfsScoreOps(adj [][]int, values []int, node, parent int) int64 {
	if adj[node] == nil || len(adj[node]) == 1 && adj[node][0] == parent {
		return int64(values[node])
	}

	var res int64 = 0
	for _, child := range adj[node] {
		if child != parent {
			res += dfsScoreOps(adj, values, child, node)
		}
	}

	if res < int64(values[node]) {
		return int64(res)
	}

	return int64(values[node])
}

func sumAll(arr []int) int64 {
	res := 0
	for _, num := range arr {
		res += num
	}
	return int64(res)
}

func maximumScoreAfterOperations(edges [][]int, values []int) int64 {
	adj := make([][]int, len(values))
	for _, edge := range edges {
		adj[edge[0]] = append(adj[edge[0]], edge[1])
		adj[edge[1]] = append(adj[edge[1]], edge[0])
	}

	return sumAll(values) - dfsScoreOps(adj, values, 0, -1)
}
