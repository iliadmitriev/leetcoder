
const INF = int(1e9)

func minimumObstacles(grid [][]int) int {
	dirs := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	m, n := len(grid), len(grid[0])

	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = INF
		}
	}
	dist[0][0] = 0

	hq := newDeque(m*n + 1)
	hq.pushFront([2]int{0, 0})

	for !hq.empty() {
		curNode := hq.popFront().([2]int)
		y, x := curNode[0], curNode[1]

		if y == m-1 && x == n-1 {
			return dist[y][x]
		}

		for i := range dirs {
			ny, nx := y+dirs[i][0], x+dirs[i][1]

			if ny < 0 || ny >= m || nx < 0 || nx >= n {
				continue
			}

			if dist[ny][nx] <= dist[y][x]+grid[ny][nx] {
				continue
			}

			dist[ny][nx] = dist[y][x] + grid[ny][nx]

			if grid[ny][nx] == 0 {
				hq.pushFront([2]int{ny, nx})
			} else {
				hq.pushBack([2]int{ny, nx})
			}
		}
	}

	return -1
}

type deque struct {
	data  []interface{}
	front int
	back  int
	size  int
}

// newDeque - circular ring buffer double ended queue
func newDeque(n int) deque {
	return deque{data: make([]interface{}, n), front: n / 2, back: n/2 + 1, size: n}
}

func (d *deque) pushFront(x interface{}) {
	d.data[d.front] = x
	d.front = (d.front - 1 + d.size) % d.size
}

func (d *deque) popFront() interface{} {
	d.front = (d.front + 1) % d.size
	x := d.data[d.front]
	return x
}

func (d *deque) pushBack(x interface{}) {
	d.data[d.back] = x
	d.back = (d.back + 1) % d.size
}

func (d *deque) popBack() interface{} {
	d.back = (d.back - 1 + d.size) % d.size
	x := d.data[d.back]
	return x
}

func (d *deque) empty() bool {
	return d.front == (d.back-1+d.size)%d.size
}
