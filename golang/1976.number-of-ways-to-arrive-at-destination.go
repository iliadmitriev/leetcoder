import (
	"container/heap"
	"math"
)

const (
	MOD = 1e9 + 7
	INF = math.MaxInt
)

type WeightNode struct {
	weight, node int
}

type MinDjHeap []WeightNode

func NewMinDjHeap(n int) *MinDjHeap {
	h := make(MinDjHeap, 0, n)
	return &h
}

func (h MinDjHeap) Len() int { return len(h) }
func (h MinDjHeap) Less(i, j int) bool {
	return h[i].weight < h[j].weight
}
func (h MinDjHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinDjHeap) Push(x interface{}) { *h = append(*h, x.(WeightNode)) }
func (h *MinDjHeap) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func (h *MinDjHeap) PushState(weight, node int) {
	heap.Push(h, WeightNode{weight, node})
}

func (h *MinDjHeap) PopState() (int, int) {
	v := heap.Pop(h).(WeightNode)
	return v.weight, v.node
}

func (h *MinDjHeap) NotEmpty() bool { return len(*h) > 0 }

type AdjWeightList struct {
	n    int
	list [][]WeightNode
}

func NewAdjWeightList(n int) *AdjWeightList {
	return &AdjWeightList{n, make([][]WeightNode, n)}
}

func (l *AdjWeightList) AddEdge(from, to, weight int) {
	l.list[from] = append(l.list[from], WeightNode{weight, to})
	l.list[to] = append(l.list[to], WeightNode{weight, from})
}

func (l *AdjWeightList) GetList(node int) []WeightNode {
	return l.list[node]
}

func NewSlice(n int, init int) []int {
	res := make([]int, n)
	if init == 0 {
		return res
	}

	for i := range res {
		res[i] = init
	}
	return res
}

func countPaths(n int, roads [][]int) int {
	pq := NewMinDjHeap(n)
	count := NewSlice(n, 0)
	dist := NewSlice(n, INF)
	adj := NewAdjWeightList(n)

	for _, r := range roads {
		adj.AddEdge(r[0], r[1], r[2])
	}

	pq.PushState(0, 0)
	dist[0] = 0
	count[0] = 1

	for pq.NotEmpty() {
		nodeDist, node := pq.PopState()

		for _, next := range adj.GetList(node) {
			nextNode, nextWeight := next.node, next.weight

			if nodeDist+nextWeight < dist[nextNode] {
				count[nextNode] = count[node]
				dist[nextNode] = nodeDist + nextWeight
				pq.PushState(nodeDist+nextWeight, nextNode)
			} else if nodeDist+nextWeight == dist[nextNode] {
				count[nextNode] += count[node]
				count[nextNode] %= MOD

			}
		}

	}

	return count[n-1]
}
