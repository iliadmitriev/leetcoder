func findMinHeightTrees(n int, edges [][]int) []int {
	if n <= 2 {
		res := make([]int, n)
		for i := 0; i < n; i++ {
			res[i] = i
		}
		return res
	}

	adjList := make([][]int, n)
	adjCount := make([]int, n)
	for _, edge := range edges {
		a, b := edge[0], edge[1]
		adjList[a] = append(adjList[a], b)
		adjList[b] = append(adjList[b], a)
		adjCount[a]++
		adjCount[b]++
	}

	leaves := make([]int, 0, n)
	for i := 0; i < n; i++ {
		if adjList[i] == nil {
			adjList[i] = []int{}
		} else if len(adjList[i]) == 1 {
			leaves = append(leaves, i)
		}
	}

	var leaf int

	for n > 2 {
		n -= len(leaves)
		for l := len(leaves); l > 0; l-- {
			leaf, leaves = leaves[0], leaves[1:]

			for _, child := range adjList[leaf] {

				adjCount[child]--
				if adjCount[child] == 1 {
					leaves = append(leaves, child)
				}
			}
		}
	}

	return leaves
}
