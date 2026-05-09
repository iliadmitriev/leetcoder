import (
    "container/heap"
)

type MinIntHeap []int
// Len, Less, Swap 
func (h MinIntHeap) Len() int { return len(h) }
func (h MinIntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinIntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

// Push, Pop, Top
func (h *MinIntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}
func (h *MinIntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0: n - 1]
    return x
}
func (h *MinIntHeap) Top() interface{} {
    old := *h
    return old[0]
}
func (h *MinIntHeap) Empty() bool {
    return len(*h) == 0
}

func fullBloomFlowers(flowers [][]int, people []int) []int {
    // two min heaps with integer values 
    // from flowers start and end points accordingly
    start := make(MinIntHeap, 0, len(flowers))
    end := make(MinIntHeap, 0, len(flowers))
    for _, flower := range flowers {
        start = append(start, flower[0])
        end = append(end, flower[1])
    }
    startHeap, endHeap := &start, &end
    heap.Init(startHeap)
    heap.Init(endHeap)

    // sorted indexes slice of people
    peopleSorted := make([][2]int, len(people))
    for i := range people {
        peopleSorted[i] = [2]int{ people[i], i }
    }
    sort.Slice(peopleSorted, func (i, j int) bool {
        return peopleSorted[i][0] < peopleSorted[j][0]
    })

    res := make([]int, len(people))
    count := 0
    for _, p := range peopleSorted {
        for !startHeap.Empty() && startHeap.Top().(int) <= p[0] {
            count++
            heap.Pop(startHeap)
        }
        for !endHeap.Empty() && endHeap.Top().(int) < p[0] {
            count--
            heap.Pop(endHeap)
        }
        res[p[1]] = count
    }

    return res
}