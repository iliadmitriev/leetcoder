import (
    "container/heap"
)

type IntHeap []int

type SeatManager struct {
    last int
    hq *IntHeap
}

func Constructor(n int) SeatManager {
    hq := make(IntHeap, 0)
    return SeatManager{
        last: 0,
        hq: &hq,
    }
}

func (this *SeatManager) Reserve() int {
	if this.hq.Empty() {
		this.last++
		return this.last
	}
	return heap.Pop(this.hq).(int)
}

func (this *SeatManager) Unreserve(seatNumber int)  {
    if seatNumber == this.last {
        this.last--
    } else {
        heap.Push(this.hq, seatNumber)
    }
}

// Less, Len, Swap, Empty
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h IntHeap) Empty() bool { return len(h) == 0 }
// Push, Pop
func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[:n - 1]
    return x
}