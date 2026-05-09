
import (
	"container/heap"
	"math"
)

type ThiefInfo struct {
	R, C int
	Dist int
}

type ThiefHeap []ThiefInfo

func (h ThiefHeap) Len() int            { return len(h) }
func (h ThiefHeap) Less(i, j int) bool  { return h[i].Dist > h[j].Dist }
func (h ThiefHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *ThiefHeap) Push(x interface{}) { *h = append(*h, x.(ThiefInfo)) }
func (h *ThiefHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maximumSafenessFactor(grid [][]int) int {
	ROWS, COLS := len(grid), len(grid[0])
	MAX_INT := math.MaxInt

	thieves := make([][]int, ROWS)
	q := make([][2]int, 0, ROWS*COLS)
	for r := 0; r < ROWS; r++ {
		thieves[r] = make([]int, COLS)
		for c := 0; c < COLS; c++ {
			if grid[r][c] == 1 {
				thieves[r][c] = 0
				q = append(q, [2]int{r, c})
			} else {
				thieves[r][c] = MAX_INT
			}
		}
	}

	dirs := [4][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

	for len(q) > 0 {
		node := q[0]
		q = q[1:]

		for _, dir := range dirs {
			nr, nc := node[0]+dir[0], node[1]+dir[1]
			if nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS {
				continue
			}

			if thieves[nr][nc] == MAX_INT || thieves[nr][nc] > thieves[node[0]][node[1]]+1 {
				thieves[nr][nc] = thieves[node[0]][node[1]] + 1
				q = append(q, [2]int{nr, nc})
			}
		}
	}

	hq := &ThiefHeap{}
	heap.Push(hq, ThiefInfo{R: 0, C: 0, Dist: thieves[0][0]})
	visited := make(map[[2]int]bool)
	visited[[2]int{0, 0}] = true

	for hq.Len() > 0 {
		node := heap.Pop(hq).(ThiefInfo)

		if node.R == ROWS-1 && node.C == COLS-1 {
			return node.Dist
		}

		for _, dir := range dirs {
			nr, nc := node.R+dir[0], node.C+dir[1]
			if nr < 0 || nr >= ROWS || nc < 0 || nc >= COLS {
				continue
			}

			if _, ok := visited[[2]int{nr, nc}]; ok {
				continue
			}

			nd := min(node.Dist, thieves[nr][nc])
			heap.Push(hq, ThiefInfo{R: nr, C: nc, Dist: nd})
			visited[[2]int{nr, nc}] = true
		}
	}
	return -1
}
