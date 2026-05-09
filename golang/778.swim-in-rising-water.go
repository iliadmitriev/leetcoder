
var dirs = [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

type Tile struct {
	x, y, height int
}

func (t Tile) Shift(delta [2]int) Tile {
	return Tile{t.x + delta[1], t.y + delta[0], t.height}
}

func (t Tile) Eq(y, x int) bool {
	return t.x == x && t.y == y
}

func (t *Tile) UpdateHeight(height int) {
	t.height = max(t.height, height)
}

// Bounded returns true if tile is within bounds [0..m-1][0..n-1] inclusive
func (t Tile) Bounded(m, n int) bool {
	return t.x >= 0 && t.x < n && t.y >= 0 && t.y < m
}

// WaterHeap is a min heap
type WaterHeap []Tile

// heap interface

func (w WaterHeap) Len() int           { return len(w) }
func (w WaterHeap) Less(i, j int) bool { return w[i].height < w[j].height }
func (w WaterHeap) Swap(i, j int)      { w[i], w[j] = w[j], w[i] }

func (w *WaterHeap) Push(x any) { *w = append(*w, x.(Tile)) }
func (w *WaterHeap) Pop() any {
	x := (*w)[len(*w)-1]
	*w = (*w)[:len(*w)-1]
	return x
}

// domain specific

func (w *WaterHeap) PushTile(tile Tile) {
	heap.Push(w, tile)
}

func (w *WaterHeap) PopTile() Tile {
	return heap.Pop(w).(Tile)
}

func (w *WaterHeap) IsEmpty() bool {
	return len(*w) == 0
}

// Water is the domain
type Water struct {
	WaterHeap

	grid [][]int
	vis  [][]bool
}

func NewWater(grid [][]int) *Water {
	rows, cols := len(grid), len(grid[0])

	h := make(WaterHeap, 0)
	heap.Init(&h)

	vis := make([][]bool, rows)
	for i := range vis {
		vis[i] = make([]bool, cols)
	}

	return &Water{h, grid, vis}
}

func (w *Water) MoveTo(tile Tile) {
	tile.UpdateHeight(w.grid[tile.y][tile.x])
	w.PushTile(tile)
	w.vis[tile.y][tile.x] = true
}

func (w *Water) IsVisited(tile Tile) bool {
	return w.vis[tile.y][tile.x]
}

func swimInWater(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	water := NewWater(grid)
	water.MoveTo(Tile{0, 0, grid[0][0]})

	for !water.IsEmpty() {
		tile := water.PopTile()

		if tile.Eq(m-1, n-1) {
			return tile.height
		}

		for _, dir := range dirs {
			nextTile := tile.Shift(dir)

			if !nextTile.Bounded(m, n) {
				continue
			}

			if water.IsVisited(nextTile) {
				continue
			}

			water.MoveTo(nextTile)
		}
	}

	return -1
}
