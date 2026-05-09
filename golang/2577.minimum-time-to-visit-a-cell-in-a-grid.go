import "container/heap"

type TimerQue [][3]int

func (h TimerQue) Len() int            { return len(h) }
func (h TimerQue) Less(i, j int) bool  { return h[i][0] < h[j][0] }
func (h TimerQue) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *TimerQue) Push(v interface{}) { *h = append(*h, v.([3]int)) }
func (h *TimerQue) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func minimumTime(grid [][]int) int {
	const INF = int(1e9)

	if grid[0][1] > 1 && grid[1][0] > 1 {
		return -1
	}

	DIRS := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	m, n := len(grid), len(grid[0])
	timer := make([][]int, m)
	for i := 0; i < m; i++ {
		timer[i] = make([]int, n)
		for j := 0; j < n; j++ {
			timer[i][j] = INF
		}
	}

	timer[0][0] = 0

	q := make(TimerQue, 0)
	heap.Push(&q, [3]int{0, 0, 0})

	for len(q) > 0 {
		item := heap.Pop(&q).([3]int)
		time, y, x := item[0], item[1], item[2]

		if y == m-1 && x == n-1 {
			return time
		}

		for _, d := range DIRS {
			ny, nx := y+d[0], x+d[1]

			if ny < 0 || ny >= m || nx < 0 || nx >= n {
				continue
			}

			var newTime int
			if time >= grid[ny][nx] {
				newTime = time + 1
			} else {
				newTime = grid[ny][nx] + (grid[ny][nx]-time+1)%2
			}

			if newTime < timer[ny][nx] {
				timer[ny][nx] = newTime
				heap.Push(&q, [3]int{newTime, ny, nx})
			}
		}

	}

	return -1
}
