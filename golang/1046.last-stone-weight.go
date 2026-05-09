import (
    "container/heap"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func lastStoneWeight(stones []int) int {
    hq := &IntHeap{}
    for _, stone := range stones { heap.Push(hq, stone) }
    
    for len(*hq) > 1 {
        st1 := heap.Pop(hq).(int)
        st2 := heap.Pop(hq).(int)

        if st1 - st2 > 0 {
            heap.Push(hq, st1 - st2)
        }
    }
    if len(*hq) > 0 {
        return (*hq)[0]
    }
    return 0
}