
type item struct {
	gain float64
	idx  int
}

type MaxGainHeap []item

func (h MaxGainHeap) Len() int           { return len(h) }
func (h MaxGainHeap) Less(i, j int) bool { return h[i].gain > h[j].gain }
func (h MaxGainHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxGainHeap) Push(x interface{}) {
	*h = append(*h, x.(item))
}

func (h *MaxGainHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func (h MaxGainHeap) MaxIdx() int {
	return h[0].idx
}

func (h MaxGainHeap) IsEmpty() bool {
	return len(h) == 0
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	n := len(classes)

	hq := &MaxGainHeap{}
	for i, c := range classes {
		if c[0] >= c[1] {
			continue
		}

		heap.Push(hq, item{extraGain(c[0], c[1]), i})
	}

	if hq.IsEmpty() {
		return 1.0
	}

	for ; extraStudents > 0; extraStudents-- {
		idx := hq.MaxIdx()
		heap.Pop(hq)

		classes[idx][0]++
		classes[idx][1]++

		gain := extraGain(classes[idx][0], classes[idx][1])
		heap.Push(hq, item{gain, idx})
	}

	avg := 0.0
	for _, c := range classes {
		avg += float64(c[0]) / float64(c[1])
	}

	return avg / float64(n)
}

func extraGain(count, total int) float64 {
	countF, totalF := float64(count), float64(total)
	return (countF+1)/(totalF+1) - countF/totalF
}
