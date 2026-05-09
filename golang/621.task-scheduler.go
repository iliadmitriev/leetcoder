import (
	"container/heap"
)

func leastInterval(tasks []byte, n int) int {
	// prepare data:
	// use map to count all tasks frequency, add frequency values to a heap MaxHeap
	freq := map[byte]int{}
	for _, t := range tasks {
		freq[t]++
	}
	data := make(MaxHeap, 0, len(freq))
	for _, v := range freq {
		data = append(data, v)
	}
	hq := &data
	heap.Init(hq)
	// result variable
	time := 0

	// queue of tasks
	q := make([]Item, 0, len(tasks))

	for hq.Len() > 0 || len(q) > 0 {

		// process task from MaxHeap
		if hq.Len() > 0 {
			item := heap.Pop(hq).(int) - 1
			if item > 0 {
				q = append(q, Item{item, time + n})
			}
		}

		// check if task from q can be processed
		if len(q) > 0 && q[0].time <= time {
			item := q[0]
			q = q[1:]
			heap.Push(hq, item.freq)
		}

		time++

	}

	return time
}

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type Item struct {
	freq, time int
}
