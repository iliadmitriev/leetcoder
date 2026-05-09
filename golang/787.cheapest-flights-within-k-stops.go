import (
    "container/heap"
)

func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
    conn := make(map[int][][2]int)
    for i := range flights {
        conn[flights[i][0]] = append(conn[flights[i][0]], [2]int{ flights[i][1], flights[i][2] })
    }

    hq := &HeapNode{}
    heap.Push(hq, [3]int{ 0, k + 1, src })
    vis := make([]int, n)

    for hq.Len() > 0 {
        flight := heap.Pop(hq).([3]int)
        total, stops, node := flight[0], flight[1], flight[2]

        if vis[node] > stops {
            continue
        }

        vis[node] = stops

        if node == dst {
            return total
        }

        for _, next := range conn[node] {
            child, price := next[0], next[1]
            heap.Push(hq, [3]int{ total + price, stops - 1, child })
        }
    }

    return -1
}


type HeapNode [][3]int
func (h HeapNode) Less(i, j int) bool {
    a, b := h[i], h[j]
    if a[0] == b[0] {
        return a[1] > b[1]
    }
    return a[0] < b[0]
}
func (h HeapNode) Swap(i, j int) {
    h[i], h[j] = h[j], h[i]
}
func (h HeapNode) Len() int {
    return len(h)
}
func (h *HeapNode) Push(x interface{}) {
    *h = append(*h, x.([3]int))
}
func (h *HeapNode) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0 : n - 1]
    return x
}