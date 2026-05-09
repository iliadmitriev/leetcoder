import (
	"container/heap"
	"sort"
)

type point struct {
	w, r, c int
}

type MinHeapPoint []point

func (h MinHeapPoint) Len() int            { return len(h) }
func (h MinHeapPoint) Less(i, j int) bool  { return h[i].w < h[j].w }
func (h MinHeapPoint) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeapPoint) Push(x interface{}) { *h = append(*h, x.(point)) }
func (h *MinHeapPoint) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func (h *MinHeapPoint) IsNotEmpty() bool {
	return len(*h) > 0
}

func (h *MinHeapPoint) PushPoint(w, r, c int) {
	heap.Push(h, point{w, r, c})
}

func (h *MinHeapPoint) PopPoint() (int, int) {
	x := heap.Pop(h).(point)
	return x.r, x.c
}

func (h *MinHeapPoint) TopWeight() int {
	return (*h)[0].w
}

func NewMinHeapPoint() *MinHeapPoint {
	return &MinHeapPoint{}
}

func maxPoints(grid [][]int, queries []int) []int {
	m, n := len(grid), len(grid[0])
	k := len(queries)

	dirs := [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	res := make([]int, k)
	h := NewMinHeapPoint()
	q := make([]int, k)
	vis := make([][]bool, m)
	count := 0

	for i := 0; i < m; i++ {
		vis[i] = make([]bool, n)
	}
	for i := 0; i < k; i++ {
		q[i] = i
	}

	h.PushPoint(grid[0][0], 0, 0)
	vis[0][0] = true

	sort.Slice(q, func(i int, j int) bool {
		return queries[q[i]] < queries[q[j]]
	})

	for _, i := range q {
		for h.IsNotEmpty() && h.TopWeight() < queries[i] {
			r, c := h.PopPoint()
			count++

			for _, d := range dirs {
				nr, nc := r+d[0], c+d[1]
				if nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] {
					vis[nr][nc] = true
					h.PushPoint(grid[nr][nc], nr, nc)
				}
			}
		}

		res[i] = count
	}

	return res
}
