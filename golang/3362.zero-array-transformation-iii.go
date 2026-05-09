import (
	"container/heap"
	"sort"
)

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() any {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func (h *MaxHeap) IsNotEmpty() bool {
	return len(*h) > 0
}

func (h *MaxHeap) PopMax() int {
	return heap.Pop(h).(int)
}

func (h *MaxHeap) PeekMax() int {
	return (*h)[0]
}

func (h *MaxHeap) PushInt(x int) {
	heap.Push(h, x)
}

func NewMaxHeap(size int) *MaxHeap {
	h := make(MaxHeap, 0, size)
	heap.Init(&h)
	return &h
}

func maxRemoval(nums []int, queries [][]int) int {
	m, n := len(nums), len(queries)
	diff := make([]int, m+1) // query cumulative difference
	cur := 0                 // current cumulative value
	hq := NewMaxHeap(m)      // query right bounds heap
	j := 0                   // query index

	sort.Slice(queries, func(i, j int) bool {
		return queries[i][0] < queries[j][0]
	})

	for i, num := range nums {
		cur += diff[i]
		// add all query right bounds to max heap with the same left bound
		for j < n && queries[j][0] == i {
			hq.PushInt(queries[j][1])
			j++
		}
		// pop query right bounds that cover current num index
		// and collect cumulative value greater or equal to current num
		for cur < num && hq.IsNotEmpty() && hq.PeekMax() >= i {
			cur++
			diff[hq.PopMax()+1]--
		}

		// if could not collect then early return -1
		if cur < num {
			return -1
		}
	}

	return hq.Len()
}
