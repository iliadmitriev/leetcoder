import (
    "container/heap"
)

type PQPoints struct {
    data [][2]int
    rows, cols int
}
// Less, Swap, Len
func (p PQPoints) Len() int { return len(p.data) }
func (p PQPoints) Swap(i, j int) { p.data[i], p.data[j] = p.data[j], p.data[i]}
// less function compares points based in the distance to finish (m, n)
func (p PQPoints) Less(i, j int) bool {
    return max(p.rows - p.data[i][0], p.cols - p.data[i][1]) >  max(p.rows - p.data[j][0], p.cols - p.data[j][1])
}

// Push, Pop
func (p *PQPoints) Push(x interface{}) {
    (*p).data = append((*p).data, x.([2]int))
}
func (p *PQPoints) Pop() interface{} {
    old := (*p).data
    n := len(old)
    x := old[n - 1]
    (*p).data = old[:n - 1]
    return x
}
func (p *PQPoints) IsNotEmpty() bool {
    return (*p).Len() > 0
}

func CreatePQPoints(rows, cols int) *PQPoints {
    return &PQPoints{
        data: make([][2]int, 0, rows * cols),
        rows: rows,
        cols: cols,
    }
}

func shortestPathBinaryMatrix(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    // if start or end are an obstacle then don't run algo
    if grid[0][0] == 1 || grid[m - 1][n - 1] == 1 {
        return -1
    }

    pq := CreatePQPoints(m, n)
    heap.Push(pq, [2]int{0, 0})

    distances := make([][]int, m)
    for i := range distances {
        distances[i] = make([]int, n)
        for j := range distances[i] {
            distances[i][j] = int(1e9)
        }
    }
    distances[0][0] = 1

    steps := [8][2]int {
        [2]int{-1, -1}, [2]int{-1, 0}, [2]int{-1, 1}, [2]int{0, -1},
        [2]int{0, 1}, [2]int{1, -1}, [2]int{1, 0}, [2]int{1, 1},
    }

    for pq.IsNotEmpty() {
        node := heap.Pop(pq).([2]int)

        if node[0] == m - 1 && node[1] == n - 1 {
            return distances[m - 1][n - 1]
        }

        for _, step := range steps {
            y, x := node[0] + step[0], node[1] + step[1]
            if y < 0 || y >= m || x < 0 || x >= n || grid[y][x] == 1 {
                continue
            }

            if distances[node[0]][node[1]] + 1 < distances[y][x] {
                distances[y][x] = distances[node[0]][node[1]] + 1
                heap.Push(pq, [2]int{y, x})
            }
        }
    }
    return -1
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}