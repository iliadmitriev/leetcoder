import (
  "container/heap"
)

type MinHeap []int
func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() any {
  old := *h
  n := len(old)
  x := old[n - 1]
  *h = old[:n - 1]
  return x
}

func (h *MinHeap) TopItem() int { return (*h)[0] }
func (h *MinHeap) PopItem() int { return heap.Pop(h).(int) }
func (h *MinHeap) PushItem(x int) { heap.Push(h, x) }
func (h *MinHeap) ReplaceItem(x int) int {
  old := (*h)[0]
  (*h)[0] = x

  heap.Fix(h, 0)

  return old
}

func NewMinHeap(arr []int) *MinHeap {
  h := make(MinHeap, len(arr))
  copy(h, arr)

  heap.Init(&h)
  return &h
}

func findKthLargest(nums []int, k int) int {
  h := NewMinHeap(nums[:k])

  for i := k; i < len(nums); i++ {
    if nums[i] > h.TopItem() {
      h.ReplaceItem(nums[i])
    }
  }

  return h.TopItem()
}