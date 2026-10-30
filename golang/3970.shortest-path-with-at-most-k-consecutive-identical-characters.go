import (
	"container/heap"
    "math"
)

type Item struct {
	dist, node, streak int
}

type MinItemHeap []Item

// contaner/heap implementation

func (h MinItemHeap) Less(i, j int) bool { return h[i].dist < h[j].dist }
func (h MinItemHeap) Len() int           { return len(h) }
func (h MinItemHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinItemHeap) Push(x any) {
	*h = append(*h, x.(Item))
}

func (h *MinItemHeap) Pop() any {
	old := *h
	n := len(old)
	val := old[n-1]
	*h = old[:n-1]
	return val
}

// domain Push/Pop

func NewMinItemHeap() *MinItemHeap {
	return &MinItemHeap{}
}

func (h *MinItemHeap) PushItem(dist, node, streak int) {
	heap.Push(h, Item{dist, node, streak})
}

func (h *MinItemHeap) PopItem() (int, int, int) {
	top := heap.Pop(h)
	value := top.(Item)
	return value.dist, value.node, value.streak
}

func (h *MinItemHeap) IsEmpty() bool {
    return len(*h) == 0
}

func shortestPath(n int, edges [][]int, labels string, k int) int {
    // reorganize graph "from node" -> {"to node", "weight"}
	g := make([][][2]int, n)
    for _, e := range edges {
        g[e[0]] = append(g[e[0]], [2]int{e[1], e[2]})
    }
    
    h := NewMinItemHeap() // min heap of {distance, node, streak}
	h.PushItem(0, 0, 1)   // start from node 0 with distance 0 with streak of 1 letter

    path := make([][]int, n)
    for i := range n {
        path[i] = make([]int, k + 1)
        for j := range k + 1 {
            path[i][j] = math.MaxInt
        }
    }
    path[0][1] = 0 // start path from node 0 with streak 1 is 0

    for !h.IsEmpty() {
        dist, node, streak := h.PopItem()

        if dist > path[node][streak] {
            continue
        }

        if node == n - 1 {
            return dist
        }

        for _, v := range g[node] {
            nnode, weight := v[0], v[1]

            nstreak := streak + 1
            if labels[node] != labels[nnode] {
                nstreak = 1
            }

            if nstreak > k {
                continue
            }

            ndist := dist + weight
            if ndist >= path[nnode][nstreak] {
                continue
            }

            path[nnode][nstreak] = ndist
            h.PushItem(ndist, nnode, nstreak)
        }

    }

    return -1
}