import (
	"container/heap"
)

var _INF = int(2e9)

func modifiedGraphEdges(n int, edges [][]int, source int, destination int, target int) [][]int {
	adj := make([][][2]int, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		if w == -1 {
			continue
		}

		adj[u] = append(adj[u], [2]int{v, w})
		adj[v] = append(adj[v], [2]int{u, w})
	}

	shortestPath := dijkstraShortestPath(adj, source, destination)

	if shortestPath < target {
		return nil
	}

	if shortestPath == target {
		for _, e := range edges {
			if e[2] == -1 {
				e[2] = _INF
			}
		}

		return edges
	}

	for i, edge := range edges {
		if edge[2] != -1 {
			continue
		}

		adj[edge[0]] = append(adj[edge[0]], [2]int{edge[1], 1})
		adj[edge[1]] = append(adj[edge[1]], [2]int{edge[0], 1})
		edge[2] = 1

		newDistance := dijkstraShortestPath(adj, source, destination)
		if newDistance <= target {
			edge[2] += target - newDistance

			for j := i + 1; j < len(edges); j++ {
				if edges[j][2] == -1 {
					edges[j][2] = _INF
				}
			}

			return edges
		}
	}

	return nil
}

type minHeap [][2]int

func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool { return h[i][0] < h[j][0] }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) {
	*h = append(*h, x.([2]int))
}
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func dijkstraShortestPath(adj [][][2]int, source, destination int) int {
	minDist := make([]int, len(adj))
	for i := range minDist {
		minDist[i] = _INF
	}
	minDist[source] = 0

	h := minHeap{[2]int{0, source}}
	for h.Len() > 0 {
		u := heap.Pop(&h).([2]int)[1]

		for _, child := range adj[u] {
			v, w := child[0], child[1]
			if d := minDist[u] + w; d < minDist[v] {
				minDist[v] = d
				heap.Push(&h, [2]int{d, v})
			}
		}
	}

	return minDist[destination]
}
