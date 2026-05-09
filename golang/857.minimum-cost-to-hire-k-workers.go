type Rate struct {
	MinWage float64
	Quality float64
}

type RateHeap []float64

func (h RateHeap) Len() int            { return len(h) }
func (h RateHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h RateHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *RateHeap) Push(x interface{}) { *h = append(*h, x.(float64)) }
func (h *RateHeap) Pop() interface{} {
	n := len(*h)
	x := (*h)[n-1]
	(*h) = (*h)[:n-1]
	return x
}

func mincostToHireWorkers(quality []int, wage []int, k int) float64 {
	hq := &RateHeap{}
	heap.Init(hq)

	n := len(quality)
	rates := make([]Rate, 0, n)
	for i := 0; i < n; i++ {
		rates = append(rates, Rate{
			float64(wage[i]) / float64(quality[i]),
			float64(quality[i]),
		})
	}

	sort.Slice(rates, func(i, j int) bool {
		return rates[i].MinWage < rates[j].MinWage
	})

	initRate := rates[k-1].MinWage
	initQuality := 0.0
	for i := 0; i < k; i++ {
		initQuality += rates[i].Quality
	}
	minCost := initRate * initQuality

	curQuality := 0.0

	for i := 0; i < n; i++ {
		if hq.Len() < k {
			curQuality += rates[i].Quality
			heap.Push(hq, rates[i].Quality)
		} else {
			curQuality += rates[i].Quality
			heap.Push(hq, rates[i].Quality)
			curQuality -= heap.Pop(hq).(float64)

			if minCost > rates[i].MinWage*curQuality {
				minCost = rates[i].MinWage * curQuality
			}
		}
	}

	return minCost
}
