import (
    "container/heap"
)

type IntHeap []int

// less, swap, len
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h IntHeap) Len() int { return len(h) }
// push
func (h *IntHeap) Push(x interface{}) {
    *h = append(*h, x.(int))
}
// pop
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0: n - 1]
    return x
}

type SmallestInfiniteSet struct {
    hq *IntHeap
    cache map[int]bool
    counter int
}


func Constructor() SmallestInfiniteSet {
    hq := &IntHeap{}
    cache := make(map[int]bool)
    return SmallestInfiniteSet{ hq, cache, 0 }
}


func (this *SmallestInfiniteSet) PopSmallest() int {
    if this.hq.Len() > 0 {
        smallest := heap.Pop(this.hq).(int)
        delete(this.cache, smallest)
        return smallest
    }
    this.counter++
    return this.counter
}


func (this *SmallestInfiniteSet) AddBack(num int)  {
    if num <= this.counter && !this.cache[num] {
        heap.Push(this.hq, num)
        this.cache[num] = true
    }
}


/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.PopSmallest();
 * obj.AddBack(num);
 */