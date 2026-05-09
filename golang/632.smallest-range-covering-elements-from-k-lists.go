import "container/heap"

type minHeap [][2]int

func (h *minHeap) Len() int           { return len(*h) }
func (h *minHeap) Less(i, j int) bool { return (*h)[i][0] < (*h)[j][0] }
func (h *minHeap) Swap(i, j int)      { (*h)[i], (*h)[j] = (*h)[j], (*h)[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.([2]int)) }
func (h *minHeap) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func smallestRange(nums [][]int) []int {
	n := len(nums)
	inx := make([]int, n)
	right := nums[0][0]
	h := make(minHeap, 0, n)

	for i := 0; i < n; i++ {
		heap.Push(&h, [2]int{nums[i][inx[i]], i})
		right = max(right, nums[i][inx[i]])
		inx[i]++
	}

	res := []int{h[0][0], right}

	for len(h) > 0 {
		left, i := h[0][0], h[0][1]
		heap.Pop(&h)

		if right-left < res[1]-res[0] {
			res = []int{left, right}
		}

		if inx[i] == len(nums[i]) {
			break
		}

		heap.Push(&h, [2]int{nums[i][inx[i]], i})
		right = max(right, nums[i][inx[i]])
		inx[i]++
	}

	return res
}
