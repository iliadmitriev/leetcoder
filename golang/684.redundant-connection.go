
func DFSFindCycle(src int, graph [][]int, visited []bool, parents []int) int {
	visited[src] = true

	for _, dst := range graph[src] {
		if !visited[dst] {
			parents[dst] = src
			cycle := DFSFindCycle(dst, graph, visited, parents)
			if cycle != -1 {
				return cycle
			}

		} else if dst != parents[src] {
			parents[dst] = src
			return dst
		}
	}

	return -1
}

func findRedundantConnection(edges [][]int) []int {
	N := len(edges) + 1
	visited := make([]bool, N)
	parents := make([]int, N)
	graph := make([][]int, N)

	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], e[1])
		graph[e[1]] = append(graph[e[1]], e[0])
	}

	cycleStart := DFSFindCycle(1, graph, visited, parents)

	cycle := make([]bool, N)
	cycle[cycleStart] = true

	for node := parents[cycleStart]; node != cycleStart; node = parents[node] {
		cycle[node] = true
	}

	for i := len(edges) - 1; i >= 0; i-- {
		u, v := edges[i][0], edges[i][1]
		if cycle[u] && cycle[v] {
			return edges[i]
		}
	}

	return nil
}
