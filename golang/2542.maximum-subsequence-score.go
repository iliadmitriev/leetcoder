import (
    "container/heap"
)

type MinHeapContainer [][2]int

func NewMinHeap(data MinHeapContainer) *MinHeapContainer {
    res := make(MinHeapContainer, 0, len(data))
    for _, v := range data {
        res = append(res, v)
    }
    heap.Init(&res)
    return &res
}
// Less, Len, Swap
func (h MinHeapContainer) Less(i, j int) bool { return h[i][0] < h[j][0] }
func (h MinHeapContainer) Len() int { return len(h) }
func (h MinHeapContainer) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
// Push
func (h *MinHeapContainer) Push(x interface{}) {
    *h = append(*h, x.([2]int))
}
// Pop
func (h *MinHeapContainer) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0: n - 1]
    return x
}
// Top
func (h *MinHeapContainer) Top() interface{} {
    p := *h
    return p[0]
}
// Empty
func (h *MinHeapContainer) Empty() bool {
    return h.Len() == 0
}

func maxScore(nums1 []int, nums2 []int, k int) int64 {
    if len(nums1) == k {
        return acc(nums1, 0, func(res int64, val int) int64 {
            return res + int64(val)
        }) * int64(minArr(nums2))
    }

    data := make([][2]int, len(nums1))
    for i := 0; i < len(nums1); i++ {
        data[i] = [2]int{ nums2[i], nums1[i] }
    }
    sort.Slice(data, func (i, j int) bool {
        return data[i][1] > data[j][1]
    })

    // min Heap
    hq := NewMinHeap(data[:k])

    curSum := int64(0)
    for _, val := range data[:k] {
        curSum += int64(val[1])
    }

    res := curSum * int64(hq.Top().([2]int)[0])

    for i := k; i < len(data); i++ {
        curSum -= int64(heap.Pop(hq).([2]int)[1])
        curSum += int64(data[i][1])
        heap.Push(hq, data[i])
        res = max(res, curSum * int64(hq.Top().([2]int)[0]))
    }
    return res
}

func acc(arr []int, start int64, fn func (int64, int) int64) int64 {
    for _, val := range arr {
        start = fn(start, val)
    }
    return start
}

func minArr(arr []int) int {
    res := arr[0]
    for _, val := range arr {
        if res > val {
            res = val
        }
    }
    return res
}

func min(a, b int64) int64 {
    if a < b {
        return a
    }
    return b
}

func max(a, b int64) int64 {
    if a > b {
        return a
    }
    return b
}