import (
	"container/heap"
	"math"
)

type Item struct {
	d, r, c int
}

type MinHeapItem []Item

func NewMinHeapItem(n int) *MinHeapItem {
	h := make(MinHeapItem, 0, n)
	heap.Init(&h)
	return &h
}

// heap interface
func (h MinHeapItem) Len() int           { return len(h) }
func (h MinHeapItem) Less(i, j int) bool { return h[i].d < h[j].d }
func (h MinHeapItem) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeapItem) Push(x any)        { *h = append(*h, x.(Item)) }
func (h *MinHeapItem) Pop() any {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

// domain specific
func (h *MinHeapItem) Top() Item                { return (*h)[0] }
func (h *MinHeapItem) IsNotEmpty() bool         { return len(*h) > 0 }
func (h *MinHeapItem) PopItem() (int, int, int) { v := heap.Pop(h).(Item); return v.d, v.r, v.c }
func (h *MinHeapItem) PushItem(d, r, c int)     { heap.Push(h, Item{d, r, c}) }

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
	dist := NewMatrix(m, n, math.MaxInt)
	dist[0][0] = 0
	q := NewMinHeapItem(m * n)
	q.PushItem(0, 0, 0)

	for q.IsNotEmpty() {
		d, r, c := q.PopItem()
		if r == m-1 && c == n-1 {
			return d
		}

		for _, dir := range dirs {
			rr, cc := r+dir[0], c+dir[1]
			if rr < 0 || rr >= m || cc < 0 || cc >= n {
				continue
			}

			if dd := max(d, moveTime[rr][cc]) + 1; dd < dist[rr][cc] {
				dist[rr][cc] = dd
				q.PushItem(dd, rr, cc)
			}
		}
	}

	return -1
}
