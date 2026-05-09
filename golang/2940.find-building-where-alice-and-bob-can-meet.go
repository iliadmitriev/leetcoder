import "container/heap"

type (
	pair          [2]int
	PriorityQueue []pair
)

func (pq PriorityQueue) Len() int            { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool  { return pq[i][0] < pq[j][0] }
func (pq PriorityQueue) Swap(i, j int)       { pq[i], pq[j] = pq[j], pq[i] }
func (pq PriorityQueue) Empty() bool         { return len(pq) == 0 }
func (pq *PriorityQueue) PeekHeight() int    { return (*pq)[0][0] }
func (pq *PriorityQueue) PeekIndex() int     { return (*pq)[0][1] }
func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(pair)) }
func (pq *PriorityQueue) Pop() interface{} {
	x := (*pq)[len(*pq)-1]
	*pq = (*pq)[:len(*pq)-1]
	return x
}

func leftmostBuildingQueries(heights []int, queries [][]int) []int {
	n, m := len(heights), len(queries)
	res := make([]int, m)
	for i := range res {
		res[i] = -1
	}

	data := make([][]pair, n)
	for i, q := range queries {
		left, right := q[0], q[1]
		if left > right {
			left, right = right, left
		}

		if left == right || heights[left] < heights[right] {
			res[i] = right
			continue
		}

		bothHeight := max(heights[left], heights[right])
		data[right] = append(data[right], pair{bothHeight, i})
	}

	pq := make(PriorityQueue, 0, n)

	for i, h := range heights {
		for _, p := range data[i] {
			heap.Push(&pq, p)
		}

		for !pq.Empty() && pq.PeekHeight() < h {
			res[pq.PeekIndex()] = i
			heap.Pop(&pq)
		}
	}

	return res
}
