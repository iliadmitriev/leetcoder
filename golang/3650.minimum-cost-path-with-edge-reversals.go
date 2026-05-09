import (
	"container/heap"
)

type NodeMinHeap [][2]int // h[weight; node]

func NewNodeMinHeap(cap int) *NodeMinHeap {
	h := make(NodeMinHeap, 0, cap)
	return &h
}

func (h NodeMinHeap) Len() int           { return len(h) }
func (h NodeMinHeap) Less(i, j int) bool { return h[i][0] < h[j][0] }
func (h NodeMinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *NodeMinHeap) Push(x any)        { *h = append(*h, x.([2]int)) }
func (h *NodeMinHeap) Pop() any          { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

// domain
func (h *NodeMinHeap) Empty() bool       { return len(*h) == 0 }
func (h *NodeMinHeap) TopItem() [2]int   { return (*h)[0] }
func (h *NodeMinHeap) PopItem() [2]int   { return heap.Pop(h).([2]int) }
func (h *NodeMinHeap) PushItem(x [2]int) { heap.Push(h, x) }

func minCost(n int, edges [][]int) int {
	start := 0
	end := n - 1
	adj := make([][][2]int, n) // adjacency lists node -> [next node; edge weight]
	weights := make([]int, n)  // current minimal weights of nodes
	h := NewNodeMinHeap(n)     // minimal heap

	for i := range weights {
		weights[i] = -1 // infinity
	}

	for _, edge := range edges {
		from, to, w := edge[0], edge[1], edge[2]
		adj[from] = append(adj[from], [2]int{to, w})
		adj[to] = append(adj[to], [2]int{from, 2 * w})
	}

	// start 0
	h.PushItem([2]int{0, start})
	weights[0] = 0

	for !h.Empty() {

		item := h.PopItem()
		node, weight := item[1], item[0]

    if weights[node] != -1 && weights[node] < weight {
      continue
    }

		if node == end {
			return weight
		}

		for _, edge := range adj[node] {
			nextNode, nextWeight := edge[0], weight+edge[1]

			if weights[nextNode] == -1 || weights[nextNode] > nextWeight {
				weights[nextNode] = nextWeight
				h.PushItem([2]int{nextWeight, nextNode})
			}

		}
	}

	return -1
}