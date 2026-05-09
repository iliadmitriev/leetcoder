import "container/heap"

type TPoint struct {
	r, c int
}

func (p *TPoint) append(dir [2]int) TPoint {
	return TPoint{p.r + dir[0], p.c + dir[1]}
}

func (p *TPoint) checkBound(NROWS, NCOLS int) bool {
	return p.r >= 0 && p.r < NROWS && p.c >= 0 && p.c < NCOLS
}

type HItem struct {
	height int
	p      TPoint
}

type TMinHeap []HItem

func NewTMinHeap(size int) *TMinHeap {
	v := make(TMinHeap, 0, size)
	return &v
}

// heap

func (h TMinHeap) Len() int           { return len(h) }
func (h TMinHeap) Less(i, j int) bool { return h[i].height < h[j].height }
func (h TMinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *TMinHeap) Push(x any) {
	*h = append(*h, x.(HItem))
}

func (h *TMinHeap) Pop() any {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func (h *TMinHeap) PushHItem(item HItem) {
	heap.Push(h, item)
}

func (h *TMinHeap) PopHItem() HItem {
	return heap.Pop(h).(HItem)
}

func (h *TMinHeap) NotEmpty() bool {
	return len(*h) > 0
}

func trapRainWater(heightMap [][]int) int {
	NROWS, NCOLS := len(heightMap), len(heightMap[0])
	res := 0
	maxHeight := 0
	visited := make([][]bool, NROWS)
	DIRS := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for i := range visited {
		visited[i] = make([]bool, NCOLS)
	}
	q := NewTMinHeap(NROWS * NCOLS)

	for r := range NROWS {
		q.PushHItem(HItem{heightMap[r][0], TPoint{r, 0}})
		q.PushHItem(HItem{heightMap[r][NCOLS-1], TPoint{r, NCOLS - 1}})
		visited[r][0] = true
		visited[r][NCOLS-1] = true
	}

	for c := 1; c < NCOLS-1; c++ {
		q.PushHItem(HItem{heightMap[0][c], TPoint{0, c}})
		q.PushHItem(HItem{heightMap[NROWS-1][c], TPoint{NROWS - 1, c}})
		visited[0][c] = true
		visited[NROWS-1][c] = true
	}

	for q.NotEmpty() {
		item := q.PopHItem()
		if item.height > maxHeight {
			maxHeight = item.height
		}

		res += maxHeight - item.height

		curPoint := item.p

		for _, dir := range DIRS {
			nextPoint := curPoint.append(dir)

			if nextPoint.checkBound(NROWS, NCOLS) && !visited[nextPoint.r][nextPoint.c] {
				visited[nextPoint.r][nextPoint.c] = true
				q.PushHItem(HItem{heightMap[nextPoint.r][nextPoint.c], nextPoint})
			}
		}

	}

	return res
}
