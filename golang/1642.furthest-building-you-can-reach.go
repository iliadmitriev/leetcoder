import (
    "container/heap"
)

func furthestBuilding(heights []int, bricks int, ladders int) int {
    hq := &MinHeap{}
    heap.Init(hq)
    
    for i := 0; i < len(heights) - 1; i++ {
        diff := heights[i + 1] - heights[i]
        if diff <= 0 {
            continue
        }

        heap.Push(hq, diff)

        if hq.Len() > ladders {
            bricks -= hq.TopInt()
            _ = heap.Pop(hq)
        }

        if bricks < 0 {
            return i
        }
    }

    return len(heights) - 1
}

type MinHeap []int

func (h *MinHeap) Len() int { return len(*h) }

func (h *MinHeap) Swap(i, j int) { (*h)[i], (*h)[j] = (*h)[j], (*h)[i] }

func (h *MinHeap) Less(i, j int) bool { return (*h)[i] < (*h)[j] }

func (h *MinHeap) TopInt() int { return (*h)[0] }

func (h *MinHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
    r := *h
    n := len(r)
    x := r[n - 1]
    *h = r[0 : n - 1]
    return x
}
