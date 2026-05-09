import (
   "container/heap"
   "math"
)

// object type
type Effort struct {
    effort int
    row, col int
}

type Efforts []Effort

type Pos struct {
    row, col int
}

// len, swap, less callbacks
func (e Efforts) Len() int { return len(e) }
func (e Efforts) Swap(i, j int) { e[i], e[j] = e[j], e[i] }
func (e Efforts) Less(i, j int) bool { return e[i].effort < e[j].effort }
// push to, pop from underlying containers methods
func (e *Efforts) Push(x interface{}) {
    *e = append(*e, x.(Effort))
}

func (e *Efforts) Pop() interface{} {
    old := *e
    n := len(old)
    x := old[n - 1]
    *e = old[0: n - 1]
    return x
}

// get absolute value
func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

// get max value of two values
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func minimumEffortPath(heights [][]int) int {
    rows, cols := len(heights), len(heights[0])

    hq := &Efforts{ Effort{0, 0, 0} }

    best := make(map[Pos]int)
    best[Pos{0, 0}] = 0

    // val, ok := best[Pos{1, 0}]
    // if !ok { val = math.MaxInt }

    phases := []int{-1, 0, 1, 0, -1}

    for len(*hq) > 0 {
        curr := heap.Pop(hq).(Effort)

        if curr.row == rows - 1 && curr.col == cols - 1 {
            return curr.effort
        }

        for i := 0; i < 4; i++ {
            nrow := curr.row + phases[i]
            ncol := curr.col + phases[i + 1]

            if 0 <= nrow && nrow < rows && 0 <= ncol && ncol < cols {
                // get previous best effort from cache or Infinite value
                prevEffort, ok := best[Pos{nrow, ncol}]
                if !ok { prevEffort = math.MaxInt }

                // calculate new effort
                newEffort := max(
                    curr.effort,
                    abs(heights[curr.row][curr.col] - heights[nrow][ncol]),
                )
                if newEffort < prevEffort {
                    best[Pos{nrow, ncol}] = newEffort
                    heap.Push(hq, Effort{newEffort, nrow, ncol})
                }
            }

        }
    }

    return 0
}