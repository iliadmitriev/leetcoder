import (
	"container/heap"
	"sort"
)

type MinEventHeap []int

// --- heap Interface methods ---

func (h MinEventHeap) Len() int           { return len(h) }
func (h MinEventHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinEventHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinEventHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MinEventHeap) Pop() any {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

// --- domain specific methods ---

func (h *MinEventHeap) PushEvent(e int) { heap.Push(h, e) }

func (h *MinEventHeap) PopEvent() int {
	return heap.Pop(h).(int)
}

func (h *MinEventHeap) TopEvent() int {
	return (*h)[0]
}

func (h *MinEventHeap) IsEmpty() bool {
	return len(*h) == 0
}

func maxEvents(events [][]int) int {
	n := len(events)
	day, i, maxEv := 1, 0, 0

	// sort events by start time
	sort.Slice(events, func(i, j int) bool {
		return events[i][0] < events[j][0]
	})

	hq := &MinEventHeap{}

	for i < n || !hq.IsEmpty() {
		// fast forward if there are no more events to attend
		if hq.IsEmpty() {
			day = events[i][0]
		}

		// add all event that can be possibly attended
		for i < n && events[i][0] <= day {
			hq.PushEvent(events[i][1])
			i++
		}

		// attend the event with the earliest end time
		hq.PopEvent()
		maxEv++
		day++

		// remove all events that have ended (impossible to attend)
		for !hq.IsEmpty() && hq.TopEvent() < day {
			hq.PopEvent()
		}
	}

	return maxEv
}
