func minOperations(nums []int, k int) int {
	ops := 0
	hq := NewMinIntHeapCopy(nums)

	for hq.Len() > 1 && hq.Top() < k {
		ops++

		a, b := hq.PopInt(), hq.PopInt()
		hq.PushInt(2*a + b)
	}

	return ops
}

type minIntHeap []int

func (h minIntHeap) Len() int            { return len(h) }
func (h minIntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h minIntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minIntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minIntHeap) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func NewMinIntHeapCopy(arr []int) *minIntHeap {
	hq := make(minIntHeap, len(arr))

	copy(hq, arr)
	heap.Init(&hq)

	return &hq
}

func (h *minIntHeap) PushInt(x int) { heap.Push(h, x) }
func (h *minIntHeap) PopInt() int   { return heap.Pop(h).(int) }
func (h *minIntHeap) Top() int      { return (*h)[0] }
