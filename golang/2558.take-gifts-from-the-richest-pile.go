
type MaxHeapSqrt []int

func (h MaxHeapSqrt) Len() int           { return len(h) }
func (h MaxHeapSqrt) Less(i, j int) bool { return h[i] > h[j] }
func (h MaxHeapSqrt) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeapSqrt) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MaxHeapSqrt) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func (h *MaxHeapSqrt) Top() int { return (*h)[0] }

func pickGifts(gifts []int, k int) int64 {
	h := MaxHeapSqrt(gifts)
	heap.Init(&h)

	for ; k > 0; k-- {
		v := h.Top()
		if v == 1 {
			break
		}

		m := int(math.Sqrt(float64(v)))

		_ = heap.Pop(&h)
		heap.Push(&h, m)
	}

	res := 0
	for _, v := range h {
		res += v
	}

	return int64(res)
}
