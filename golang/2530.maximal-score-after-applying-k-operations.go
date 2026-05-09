import "container/heap"

type maxHeap []int

func (h *maxHeap) Len() int           { return len(*h) }
func (h *maxHeap) Less(i, j int) bool { return (*h)[i] > (*h)[j] }
func (h *maxHeap) Swap(i, j int)      { (*h)[i], (*h)[j] = (*h)[j], (*h)[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *maxHeap) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func maxKelements(nums []int, k int) int64 {
	h := maxHeap(nums)
	heap.Init(&h)

	score := 0

	for k > 0 {
		x := heap.Pop(&h).(int)

		if x == 1 {
			score += k
			k = 0
		} else {
			score += x
			heap.Push(&h, divideCeil(x, 3))
			k--
		}
	}

	return int64(score)
}

func divideCeil(x, y int) int {
	if x%y > 0 {
		return x/y + 1
	}

	return x / y
}
