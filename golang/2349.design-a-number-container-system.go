import "container/heap"

type minIdxHeap []int

func (h minIdxHeap) Len() int           { return len(h) }
func (h minIdxHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h minIdxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *minIdxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *minIdxHeap) Pop() interface{} {
	a := *h
	v := a[len(a)-1]
	*h = a[:len(a)-1]
	return v
}

func (h *minIdxHeap) PushIdx(x int) {
	heap.Push(h, x)
}

func (h *minIdxHeap) PopIdx() {
	_ = heap.Pop(h).(int)
}

func (h *minIdxHeap) TopIdx() int {
	return (*h)[0]
}

func (h *minIdxHeap) Empty() bool {
	return h.Len() == 0
}

type NumberContainers struct {
	nums map[int]int
	inx  map[int]*minIdxHeap
}

func Constructor() NumberContainers {
	return NumberContainers{map[int]int{}, map[int]*minIdxHeap{}}
}

func (this *NumberContainers) Change(index int, number int) {
	this.nums[index] = number

	if _, ok := this.inx[number]; !ok {
		this.inx[number] = &minIdxHeap{}
	}

	this.inx[number].PushIdx(index)
}

func (this *NumberContainers) Find(number int) int {
	if _, ok := this.inx[number]; !ok {
		return -1
	}

	mh := this.inx[number]

	for !mh.Empty() {
		if this.nums[mh.TopIdx()] == number {
			return mh.TopIdx()
		} else {
			mh.PopIdx()
		}
	}

	return -1
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Change(index,number);
 * param_2 := obj.Find(number);
 */