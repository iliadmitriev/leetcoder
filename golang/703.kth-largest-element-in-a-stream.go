import (
	"container/heap"
)

type MinHeap []int

func NewMinHeap(data []int) *MinHeap {
	h := make(MinHeap, len(data))
	copy(h, data)
	heap.Init(&h)
	return &h
}

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type KthLargest struct {
	Pos  int
	Data *MinHeap
}

func Constructor(k int, nums []int) KthLargest {
	this := KthLargest{
		Pos:  k,
		Data: NewMinHeap(nums),
	}

	for this.Data.Len() > this.Pos {
		heap.Pop(this.Data)
	}

	return this
}

func (this *KthLargest) Add(val int) int {
	heap.Push(this.Data, val)
	if this.Data.Len() > this.Pos {
		heap.Pop(this.Data)
	}

	return (*this.Data)[0]
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */