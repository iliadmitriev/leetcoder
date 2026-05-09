import "container/heap"

type MinCardHeap []int

func (h MinCardHeap) Len() int {
	return len(h)
}

func (h MinCardHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h MinCardHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinCardHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinCardHeap) Pop() interface{} {
	n := len(*h)
	x := (*h)[n-1]
	*h = (*h)[:n-1]
	return x
}

func (h *MinCardHeap) Top() int {
	return (*h)[0]
}

func isNStraightHand(hand []int, groupSize int) bool {
	if (len(hand) % groupSize) != 0 {
		return false
	}

	counts := make(map[int]int, len(hand))
	for _, card := range hand {
		counts[card]++
	}
	minHeap := make(MinCardHeap, 0, len(counts))
	for card := range counts {
		minHeap = append(minHeap, card)
	}
	heap.Init(&minHeap)

	for minHeap.Len() > 0 {
		minCard := minHeap.Top()
		for card := minCard; card < minCard+groupSize; card++ {
			if counts[card] == 0 {
				return false
			}
			counts[card]--

			if counts[card] == 0 {
				if minHeap.Top() != card {
					return false
				}
				heap.Pop(&minHeap)
			}
		}
	}

	return true
}
