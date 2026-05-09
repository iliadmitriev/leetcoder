import (
	"container/heap"
)

type MinHeapQue [][2]int

func (h MinHeapQue) Len() int { return len(h) }
func (h MinHeapQue) Less(i, j int) bool {
	if h[i][0] == h[j][0] {
		return h[i][1] < h[j][1]
	}

	return h[i][0] < h[j][0]
}
func (h MinHeapQue) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeapQue) Push(x interface{}) { *h = append(*h, x.([2]int)) }
func (h *MinHeapQue) Pop() interface{} {
	v := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return v
}
func (h MinHeapQue) IsEmpty() bool { return len(h) == 0 }
func (h MinHeapQue) Peek() int     { return h[0][0] }

func continuousSubarrays(nums []int) int64 {
	minHeap := MinHeapQue{}
	maxHeap := MinHeapQue{}
	count := 0

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	for left, right := -1, 0; right < len(nums); right++ {

		for !minHeap.IsEmpty() && abs(minHeap.Peek()-nums[right]) > 2 {
			left = heap.Pop(&minHeap).([2]int)[1]
		}

		for !maxHeap.IsEmpty() && abs(maxHeap.Peek()+nums[right]) > 2 {
			left = heap.Pop(&maxHeap).([2]int)[1]
		}

		heap.Push(&minHeap, [2]int{nums[right], right})
		heap.Push(&maxHeap, [2]int{-nums[right], right})
		count += right - left
	}

	return int64(count)
}
