import "container/heap"

type MinIdxQue [][2]int

func (h MinIdxQue) Len() int { return len(h) }
func (h MinIdxQue) Less(i, j int) bool {
	if h[i][0] == h[j][0] {
		return h[i][1] < h[j][1]
	}
	return h[i][0] < h[j][0]
}
func (h MinIdxQue) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MinIdxQue) Push(v interface{}) {
	*h = append(*h, v.([2]int))
}

func (h *MinIdxQue) Pop() interface{} {
	a := *h
	v := a[len(a)-1]
	*h = a[:len(a)-1]
	return v
}

func (h MinIdxQue) Empty() bool {
	return len(h) == 0
}

func findScore(nums []int) int64 {
	score := 0
	n := len(nums)

	h := make(MinIdxQue, 0, n)
	for i, v := range nums {
		h.Push([2]int{v, i})
	}

	heap.Init(&h)

	marked := make([]bool, n)

	for !h.Empty() {
		top := heap.Pop(&h).([2]int)

		if marked[top[1]] {
			continue
		}

		score += top[0]

		marked[top[1]] = true

		if top[1] > 0 {
			marked[top[1]-1] = true
		}

		if top[1] < n-1 {
			marked[top[1]+1] = true
		}
	}

	return int64(score)
}
