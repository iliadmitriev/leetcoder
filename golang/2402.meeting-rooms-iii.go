import (
	"container/heap"
	"sort"
)

func mostBooked(n int, meetings [][]int) int {
	sort.Slice(meetings, func(i, j int) bool {
		if meetings[i][0] == meetings[j][0] {
			return meetings[i][1] < meetings[j][1]
		}
		return meetings[i][0] < meetings[j][0]
	})

	available := &MinHeapRoom{}
	for i := range n {
		*available = append(*available, i)
	}
	heap.Init(available)

	occupied := &MinHeapMeetings{}

	res := make([]int, n)

	for _, meeting := range meetings {
		start, end := meeting[0], meeting[1]

		for occupied.Len() > 0 && occupied.TopEnding() <= start {
			_, room := occupied.PopMeeting()
			available.PushRoom(room)
		}

		if available.Len() > 0 {
			room := available.PopRoom()
			occupied.PushMeeting(end, room)
			res[room]++
		} else {
			ending, room := occupied.PopMeeting()
			diff := end - start
			occupied.PushMeeting(ending+diff, room)
			res[room]++
		}
	}

	maxIdx := 0
	for i := 1; i < n; i++ {
		if res[maxIdx] < res[i] {
			maxIdx = i
		}
	}

	return maxIdx
}

type MinHeapRoom []int

func (h *MinHeapRoom) Len() int           { return len(*h) }
func (h *MinHeapRoom) Less(i, j int) bool { return (*h)[i] < (*h)[j] }
func (h *MinHeapRoom) Swap(i, j int)      { (*h)[i], (*h)[j] = (*h)[j], (*h)[i] }
func (h *MinHeapRoom) Push(x any)         { *h = append(*h, x.(int)) }
func (h *MinHeapRoom) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func (h *MinHeapRoom) PushRoom(room int) { heap.Push(h, room) }
func (h *MinHeapRoom) PopRoom() int      { return heap.Pop(h).(int) }

type MinHeapMeetings [][2]int

func (h *MinHeapMeetings) Len() int      { return len(*h) }
func (h *MinHeapMeetings) Swap(i, j int) { (*h)[i], (*h)[j] = (*h)[j], (*h)[i] }
func (h *MinHeapMeetings) Less(i, j int) bool {
	if (*h)[i][0] == (*h)[j][0] {
		return (*h)[i][1] < (*h)[j][1]
	}
	return (*h)[i][0] < (*h)[j][0]
}
func (h *MinHeapMeetings) Push(x any) { *h = append(*h, x.([2]int)) }
func (h *MinHeapMeetings) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func (h *MinHeapMeetings) TopEnding() int               { return (*h)[0][0] }
func (h *MinHeapMeetings) TopRoom() int                 { return (*h)[0][1] }
func (h *MinHeapMeetings) PushMeeting(ending, room int) { heap.Push(h, [2]int{ending, room}) }
func (h *MinHeapMeetings) PopMeeting() (int, int)       { x := heap.Pop(h).([2]int); return x[0], x[1] }
