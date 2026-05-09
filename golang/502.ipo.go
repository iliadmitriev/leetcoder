
import (
	"container/heap"
	"sort"
)

type MaxProfit []int

func (h MaxProfit) Len() int            { return len(h) }
func (h MaxProfit) Less(i, j int) bool  { return h[i] > h[j] }
func (h MaxProfit) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MaxProfit) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *MaxProfit) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
func (h MaxProfit) Top() int { return h[0] }

func maxArr(arr []int) int {
	m := arr[0]
	for _, v := range arr {
		if v > m {
			m = v
		}
	}
	return m
}

func sumArr(arr []int) int {
	s := 0
	for _, v := range arr {
		s += v
	}
	return s
}

func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	// optimization: if we have enough capital to do all the projects
	if w >= maxArr(capital) {
		// get all projects
		if k >= len(profits) {
			return w + sumArr(profits)
		}
		// get top k most profitable projects
		sort.Ints(profits)
		return w + sumArr(profits[len(profits)-k:])
	}

	projects := make([][2]int, 0, len(profits))
	for i := range profits {
		projects = append(projects, [2]int{capital[i], profits[i]})
	}
	sort.Slice(projects, func(i, j int) bool { return projects[i][0] < projects[j][0] })

	pq := make(MaxProfit, 0, k)

	j := 0
	for ; k > 0; k-- {
		for j < len(projects) && projects[j][0] <= w {
			heap.Push(&pq, projects[j][1])
			j++
		}
		if pq.Len() == 0 {
			break
		}
		w += heap.Pop(&pq).(int)
	}

	return w
}
