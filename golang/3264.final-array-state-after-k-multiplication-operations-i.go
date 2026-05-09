import "container/heap"

type Heap [][2]int

func (h Heap) Len() int { return len(h) }
func (h Heap) Less(i, j int) bool {
	if h[i][1] == h[j][1] {
		return h[i][0] < h[j][0]
	}
	return h[i][1] < h[j][1]
}
func (h Heap) Swap(i, j int)           { h[i], h[j] = h[j], h[i] }
func (h *Heap) Push(x interface{})     { *h = append(*h, x.([2]int)) }
func (h *Heap) Pop() interface{}       { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }
func (h *Heap) HeapPopIndex() int      { return heap.Pop(h).([2]int)[0] }
func (h *Heap) HeapPushIndex(i, v int) { heap.Push(h, [2]int{i, v}) }

func getFinalState(nums []int, k int, multiplier int) []int {
	hq := make(Heap, 0, len(nums))
	for i, v := range nums {
		hq.HeapPushIndex(i, v)
	}

	for ; k > 0; k-- {
		index := hq.HeapPopIndex()
		nums[index] *= multiplier
		hq.HeapPushIndex(index, nums[index])
	}

	return nums
}
