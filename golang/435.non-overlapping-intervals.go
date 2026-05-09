/*

-1
[[1 2] [1 3] [2 3] [3 4]]

2

*/
import (
  "math"
	"container/heap"
)

type MinHeap []int

// Heap interface
func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() any          { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

// domain
func (h *MinHeap) PushItem(x int) { heap.Push(h, x) }
func (h *MinHeap) PopItem() int   { return heap.Pop(h).(int) }
func (h *MinHeap) TopItem() int   { return (*h)[0] }
func (h *MinHeap) Empty() bool    { return len(*h) == 0 }

func eraseOverlapIntervals(intervals [][]int) int {
	// O(n log n)
  /* Sort by end
  __
  ___
  _______
    _____
  __________
     _______
       __________
          _______
                ______
  */
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})

	rem := 0 // number of intervals to remove
	prev := math.MinInt

	for _, iv := range intervals {
		start, end := iv[0], iv[1]

		// if overlap
		if prev > start {
      // remove current interval
			rem++
		} else {
      // do not remove current interval
      // move to next
			prev = end
		}
	}

	return rem
}