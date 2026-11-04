import (
	"container/heap"
)

type Heap struct {
	data []int
	less func(int, int) bool
}

func (h Heap) Len() int           { return len(h.data) }
func (h Heap) Less(i, j int) bool { return h.less(h.data[i], h.data[j]) }
func (h Heap) Swap(i, j int)      { h.data[i], h.data[j] = h.data[j], h.data[i] }

func (h *Heap) Push(x any) {
	h.data = append(h.data, x.(int))
}

func (h *Heap) Pop() any {
	n := len(h.data)
	x := h.data[n-1]
	h.data = h.data[:n-1]

	return x
}

type HeapSum struct {
	sum, size int
	removed   map[int]int
	q         Heap
}

func (h *HeapSum) Top() int {
	return h.q.data[0]
}

func (h *HeapSum) Push(x int) {
	h.size++
	h.sum += x
	heap.Push(&h.q, x)
}

func (h *HeapSum) Pop() int {
	v := heap.Pop(&h.q)
	h.prune()

	x := v.(int)
	h.size--
	h.sum -= x

	return x
}

func (h *HeapSum) Size() int {
	return h.size // real size (considering the lazy removed elements)
}

func (h *HeapSum) Sum() int {
	return h.sum // real sum (considering the lazy removed elements)
}

func (h *HeapSum) Remove(x int) {
	h.removed[x]++
	h.size--
	h.sum -= x

	h.prune()
}

func (h *HeapSum) prune() {
	for len(h.q.data) > 0 {
		top := h.q.data[0]
		if _, ok := h.removed[top]; !ok {
			return
		}

		h.removed[top]--
		if h.removed[top] <= 0 {
			delete(h.removed, top)
		}

		heap.Pop(&h.q)
	}
}

func NewHeapSum(n int, less func(int, int) bool) *HeapSum {
	q := Heap{
		data: make([]int, 0, n),
		less: less,
	}

	return &HeapSum{
		sum: 0, size: 0, removed: map[int]int{}, q: q,
	}
}

type BalancedWindow struct {
	upper, lower *HeapSum
}

func (b *BalancedWindow) Add(x int) {
	if b.lower.Size() == 0 || x <= b.lower.Top() {
		b.lower.Push(x)
	} else {
		b.upper.Push(x)
	}

	b.rebalance()
}

func (b *BalancedWindow) Remove(x int) {
	if x <= b.lower.Top() {
		b.lower.Remove(x)
	} else {
		b.upper.Remove(x)
	}

	b.rebalance()
}

func (b *BalancedWindow) GetOps() int {
	mid := b.lower.Top()

	return b.upper.Sum() - b.lower.Sum() + mid*(b.lower.Size()-b.upper.Size())
}

func (b *BalancedWindow) rebalance() {
	if b.lower.Size() > b.upper.Size()+1 {
		val := b.lower.Pop()
		b.upper.Push(val)
	} else if b.lower.Size() < b.upper.Size() {
		val := b.upper.Pop()
		b.lower.Push(val)
	}
}

func NewBalancedWindow(n int) *BalancedWindow {
	less := func(a, b int) bool { return a < b }
	greater := func(a, b int) bool { return a > b }

	return &BalancedWindow{
		lower: NewHeapSum(n, greater),
		upper: NewHeapSum(n, less),
	}
}

func minOperations(nums []int, x int, k int) int64 {
	n := len(nums)
	win := NewBalancedWindow(x/2 + 1)
	ops := make([]int, n)

	for r := range n {
		win.Add(nums[r])

		l := r - x + 1
		if l < 0 {
			continue
		}

		ops[r] = win.GetOps()

		win.Remove(nums[l])
	}

	dp := make([][]int, n)
	for i := range n {
		dp[i] = make([]int, k+1)
		dp[i][0] = 0

		for j := 1; j < k+1; j++ {
			dp[i][j] = math.MaxInt
		}
	}

	for j := 1; j <= k; j++ {
		if j == 1 {
			dp[x-1][j] = ops[x-1]
		} else {
			dp[j*x-1][j] = dp[(j-1)*x-1][j-1] + ops[j*x-1]
		}
	}

	for j := 1; j <= k; j++ {
		for i := j * x; i < n; i++ {
			dp[i][j] = min(dp[i-x][j-1]+ops[i], dp[i-1][j])
		}
	}

	return int64(dp[n-1][k])
}