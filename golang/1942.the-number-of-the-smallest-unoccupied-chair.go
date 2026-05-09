import (
	"container/heap"
	"sort"
)

type MinChairHeap []int

func (h *MinChairHeap) Len() int           { return len(*h) }
func (h *MinChairHeap) Less(i, j int) bool { return (*h)[i] < (*h)[j] }
func (h *MinChairHeap) Swap(i, j int)      { (*h)[i], (*h)[j] = (*h)[j], (*h)[i] }
func (h *MinChairHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MinChairHeap) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

type MinOccupiedHeap [][2]int

func (h *MinOccupiedHeap) Len() int           { return len(*h) }
func (h *MinOccupiedHeap) Less(i, j int) bool { return (*h)[i][0] < (*h)[j][0] }
func (h *MinOccupiedHeap) Swap(i, j int)      { (*h)[i], (*h)[j] = (*h)[j], (*h)[i] }
func (h *MinOccupiedHeap) Push(x interface{}) { *h = append(*h, x.([2]int)) }
func (h *MinOccupiedHeap) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func smallestChair(times [][]int, targetFriend int) int {
	n := len(times)
	friends := make([]int, n)
	for i := 0; i < n; i++ {
		friends[i] = i
	}

	sort.Slice(friends, func(i, j int) bool {
		return times[friends[i]][0] < times[friends[j]][0]
	})

	occupiedChairs := make(MinOccupiedHeap, 0, n)
	freeChairs := make(MinChairHeap, 0, n)
	topFreeChair := 0

	for _, friend := range friends {
		start, end := times[friend][0], times[friend][1]

		for len(occupiedChairs) > 0 && occupiedChairs[0][0] <= start {
			free := heap.Pop(&occupiedChairs).([2]int)[1]

			if free+1 == topFreeChair {
				topFreeChair--
			} else {
				heap.Push(&freeChairs, free)
			}
		}

		chair := -1

		if freeChairs.Len() > 0 {
			chair = heap.Pop(&freeChairs).(int)
		} else {
			chair = topFreeChair
			topFreeChair++
		}

		if targetFriend == friend {
			return chair
		}

		heap.Push(&occupiedChairs, [2]int{end, chair})

	}

	return -1
}
