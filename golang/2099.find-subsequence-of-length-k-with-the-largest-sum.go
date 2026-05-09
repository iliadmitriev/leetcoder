import (
	"container/heap"
	"slices"
)

type (
	pair        [2]int // [value, index]
	MinHeapPair []pair
)

// ---------- heap Interface ----------
func (h MinHeapPair) Len() int      { return len(h) }
func (h MinHeapPair) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h MinHeapPair) Less(i, j int) bool {
	if h[i][0] == h[j][0] {
		return h[i][1] < h[j][1]
	}
	return h[i][0] < h[j][0]
}

func (h *MinHeapPair) Push(x interface{}) {
	*h = append(*h, x.(pair))
}

func (h *MinHeapPair) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

// ------------ domain methods -----------
func (h *MinHeapPair) PopPair() (int, int) {
	x := heap.Pop(h).(pair)
	return x[0], x[1]
}

func (h *MinHeapPair) PushPair(v, i int) {
	heap.Push(h, pair{v, i})
}

func (h *MinHeapPair) TopValue() int {
	return (*h)[0][0]
}

func maxSubsequence(nums []int, k int) []int {
	hq := make(MinHeapPair, 0, k)

	for i, num := range nums {
		if hq.Len() < k {
			hq.PushPair(num, i)
		} else if num > hq.TopValue() {
			hq.PopPair()
			hq.PushPair(num, i)
		}
	}

	slices.SortFunc(hq, func(a, b pair) int {
		if a[1] < b[1] {
			return -1
		} else if a[1] > b[1] {
			return 1
		}
		return 0
	})

	res := make([]int, k)
	for i := range k {
		res[i] = nums[hq[i][1]]
	}
	return res
}
