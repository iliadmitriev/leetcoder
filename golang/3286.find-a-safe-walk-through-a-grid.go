import "container/heap"

// State represents the current health and position in the grid
type State struct {
	health int
	r, c   int
}

// MaxHeap implements heap.Interface for a max-heap based on health
type MaxHeap []State

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i].health > h[j].health } // '>' for max-heap
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(State))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// ---------- Domain methods ----------

// NewMaxHeap creates an initialized max-heap with the given capacity hint.
func NewMaxHeap(cap int) *MaxHeap {
	h := make(MaxHeap, 0, cap)
	heap.Init(&h)
	return &h
}

// IsEmpty reports whether the heap contains no elements.
func (h *MaxHeap) IsEmpty() bool {
	return h.Len() == 0
}

// PopState removes and returns the top element as (health, r, c).
func (h *MaxHeap) PopState() (int, int, int) {
	state := heap.Pop(h).(State)
	return state.health, state.r, state.c
}

// PushState inserts a new element with the given health and coordinates.
func (h *MaxHeap) PushState(health, r, c int) {
	heap.Push(h, State{health, r, c})
}

// ---------- Solution ----------

func findSafeWalk(grid [][]int, health int) bool {
	m, n := len(grid), len(grid[0])
	sides := [4][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	finishR, finishC := m-1, n-1

	health -= grid[0][0]

	hq := NewMaxHeap(m * n)
	hq.PushState(health, 0, 0)

	vis := make([][]bool, m)
	for i := range vis {
		vis[i] = make([]bool, n)
	}
	vis[0][0] = true

	for !hq.IsEmpty() {
		h, r, c := hq.PopState()

		if r == finishR && c == finishC {
			return true
		}

		for _, side := range sides {
			nr, nc := r+side[0], c+side[1]

			if nr < 0 || nr >= m || nc < 0 || nc >= n {
				continue
			}

			newHealth := h - grid[nr][nc]
			if newHealth <= 0 || vis[nr][nc] {
				continue
			}

			vis[nr][nc] = true
			hq.PushState(newHealth, nr, nc)
		}
	}

	return false
}