import "container/heap"

type Vertex struct {
	Child int
	Prob  float64
}

type Edge struct {
	Node int
	Prob float64
}

type MaxEdgeHeap []Edge

func (h MaxEdgeHeap) Len() int           { return len(h) }
func (h MaxEdgeHeap) Less(i, j int) bool { return h[i].Prob > h[j].Prob }
func (h MaxEdgeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxEdgeHeap) Push(x interface{}) {
	*h = append(*h, x.(Edge))
}

func (h *MaxEdgeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func maxProbability(n int, edges [][]int, succProb []float64, start_node int, end_node int) float64 {
	adj := make([][]Vertex, n)
	for i := 0; i < len(edges); i++ {
		u, v := edges[i][0], edges[i][1]
		adj[u] = append(adj[u], Vertex{v, succProb[i]})
		adj[v] = append(adj[v], Vertex{u, succProb[i]})
	}

	prob := make([]float64, n)
	prob[start_node] = 1.0

	q := make(MaxEdgeHeap, 0)
	heap.Push(&q, Edge{start_node, 1.0})

	for len(q) > 0 {
		node := heap.Pop(&q).(Edge).Node

		for _, child := range adj[node] {
			if prob[child.Child] < prob[node]*child.Prob {
				prob[child.Child] = prob[node] * child.Prob

				heap.Push(&q, Edge{child.Child, prob[child.Child]})

			}
		}

	}

	return prob[end_node]
}
