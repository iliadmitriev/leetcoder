import (
	"container/heap"
)

type MaxHeap struct {
	d    [][2]int            // data (value, index)
	less func(int, int) bool // func to compare, default min
}

// interface heap.Heap
func (h MaxHeap) Less(i, j int) bool { return h.less(h.d[i][0], h.d[j][0]) }
func (h MaxHeap) Swap(i, j int)      { h.d[i], h.d[j] = h.d[j], h.d[i] }
func (h MaxHeap) Len() int           { return len(h.d) }

func (h *MaxHeap) Push(x any) { h.d = append(h.d, x.([2]int)) }
func (h *MaxHeap) Pop() any   { n := len(h.d); x := h.d[n-1]; h.d = h.d[:n-1]; return x }

// domain
func (h *MaxHeap) TopItem() [2]int   { return h.d[0] }
func (h *MaxHeap) PushItem(x [2]int) { heap.Push(h, x) }
func (h *MaxHeap) PopItem() [2]int   { return heap.Pop(h).([2]int) }
func (h *MaxHeap) Empty() bool       { return len(h.d) == 0 }
func (h *MaxHeap) ReplaceItem(x [2]int) [2]int {
	v := h.d[0]
	h.d[0] = x
	heap.Fix(h, 0)

	return v
}

func NewHeap(cap int, min bool) *MaxHeap {
	d := make([][2]int, 0, cap)
	var less func(int, int) bool

	if min {
		less = func(a, b int) bool { return a < b }
	} else {
		less = func(a, b int) bool { return a > b }
	}

	return &MaxHeap{
		d:    d,
		less: less,
	}
}

func minimumCost(nums []int, k int, dist int) int64 {

	hUsed := NewHeap(k, false)  // used max heap (value, index)
	hUnused := NewHeap(k, true) // unused min heap (value, index)
	used := make(map[int]bool)  // used indices

	cur := 0
	minSum := math.MaxInt

	for right := 1; right < len(nums); right++ {
		left := right - dist - 1 // left index of window of size dist - 1

		if left > 0 && used[left] {
			delete(used, left)
			cur -= nums[left]

			// drop values out if window scope
			for !hUnused.Empty() && hUnused.TopItem()[1] < left {
				_ = hUnused.PopItem()
			}

			// pop minimal value from unused values if it's available
			if !hUnused.Empty() {
				value := hUnused.PopItem()
				cur += value[0]
				used[value[1]] = true
				hUsed.PushItem(value)
			}
		}

		if len(used) < k-1 {
			hUsed.PushItem([2]int{nums[right], right})
			used[right] = true
			cur += nums[right]
		} else {

			// purge used max heap
			for !used[hUsed.TopItem()[1]] {
				_ = hUsed.PopItem()
			}

			if nums[right] < hUsed.TopItem()[0] {
				prev := hUsed.ReplaceItem([2]int{nums[right], right})
				cur -= prev[0]
				cur += nums[right]
				delete(used, prev[1])
				used[right] = true

				hUnused.PushItem(prev)
			} else {
				hUnused.PushItem([2]int{nums[right], right})
			}
		}

		if left >= 0 {
			minSum = min(minSum, cur)
		}

	}

	return int64(nums[0] + minSum)
}