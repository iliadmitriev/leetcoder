import (
	"container/heap"
	"math"
)

type State struct {
	// d: distance, i: index parity 0|1, r: row, c: col
	d, i, r, c int
}

// MinStateHeap is a min heap of State
type MinStateHeap []State

func NewMinStateHeap(n int) *MinStateHeap {
	h := make(MinStateHeap, 0, n)
	heap.Init(&h)
	return &h
}

func (h MinStateHeap) Len() int           { return len(h) }
func (h MinStateHeap) Less(i, j int) bool { return h[i].d < h[j].d }
func (h MinStateHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinStateHeap) Push(x any) { *h = append(*h, x.(State)) }
func (h *MinStateHeap) Pop() any {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func (h *MinStateHeap) Top() State       { return (*h)[0] }
func (h *MinStateHeap) IsNotEmpty() bool { return len(*h) > 0 }
func (h *MinStateHeap) PopState() (int, int, int, int) {
	v := heap.Pop(h).(State)
	return v.d, v.i, v.r, v.c
}
func (h *MinStateHeap) PushState(d, i, r, c int) { heap.Push(h, State{d, i, r, c}) }

// NewMatrix returns a matrix of size m*n with each cell initialized to v
func NewMatrix(m, n int, v int) [][]int {
	res := make([][]int, m)
	for i := range res {
		res[i] = make([]int, n)
		for j := range res[i] {
			res[i][j] = v
		}
	}
	return res
}

func minTimeToReach(moveTime [][]int) int {
	m, n := len(moveTime), len(moveTime[0])
	dirs := [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

	h := NewMinStateHeap(m * n)
	h.PushState(0, 0, 0, 0)
	dist := NewMatrix(m, n, math.MaxInt)
	dist[0][0] = 0

	for h.IsNotEmpty() {
		d, i, r, c := h.PopState()
		if r == m-1 && c == n-1 {
			return d
		}

		for _, dir := range dirs {
			rr, cc := r+dir[0], c+dir[1]
			if rr < 0 || rr >= m || cc < 0 || cc >= n {
				continue
			}

			dd := max(d, moveTime[rr][cc]) + 1 + i
			if dd < dist[rr][cc] {
				dist[rr][cc] = dd
				h.PushState(dd, i^1, rr, cc)
			}
		}

	}

	return -1
}
