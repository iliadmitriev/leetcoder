type Pos struct {
	y, x int
}

type State struct {
	cost int
	pos  Pos
}

type MinStateHeap []State

func (h MinStateHeap) Len() int           { return len(h) }
func (h MinStateHeap) Less(i, j int) bool { return h[i].cost < h[j].cost }
func (h MinStateHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinStateHeap) Push(x interface{}) {
	*h = append(*h, x.(State))
}

func (h *MinStateHeap) Pop() interface{} {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func (h MinStateHeap) NotEmpty() bool {
	return len(h) > 0
}

func (h *MinStateHeap) PushState(state State) {
	heap.Push(h, state)
}

func (h *MinStateHeap) PopState() State {
	return heap.Pop(h).(State)
}

const InfInt = int(1e9)

type DistMap map[Pos]int

func NewDistMap() DistMap {
	return make(DistMap)
}

func (d *DistMap) GetCost(pos Pos) int {
	if v, ok := (*d)[pos]; ok {
		return v
	}

	return InfInt
}

type Grid struct {
	maxRow, maxCol int
	dirs           [][3]int
	grid           [][]int
}

func NewGrid(grid [][]int) *Grid {
	dirs := [][3]int{
		{1, 0, 1},
		{2, 0, -1},
		{3, 1, 0},
		{4, -1, 0},
	}
	return &Grid{len(grid), len(grid[0]), dirs, grid}
}

type StepFunc func(newPos Pos, addedCost int)

func (g *Grid) Step(pos Pos, stepFunc StepFunc) {
	maxRow, maxCol := g.maxRow, g.maxCol
	for _, dir := range g.dirs {
		ny, nx := pos.y+dir[1], pos.x+dir[2]

		if ny < 0 || ny >= maxRow || nx < 0 || nx >= maxCol {
			continue
		}

		newPos := Pos{ny, nx}
		addedCost := 0

		if dir[0] != g.grid[pos.y][pos.x] {
			addedCost += 1
		}

		stepFunc(newPos, addedCost)

	}
}

func minCost(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	start, end := Pos{0, 0}, Pos{m - 1, n - 1}
	pq := MinStateHeap{State{0, start}}
	gr := NewGrid(grid)
	distMap := NewDistMap()

	for pq.NotEmpty() {
		state := pq.PopState()
		cost, pos := state.cost, state.pos

		if pos == end {
			return cost
		}

		gr.Step(pos, func(newPos Pos, addedCost int) {
			newCost := cost + addedCost
			if newCost < distMap.GetCost(newPos) {
				distMap[newPos] = newCost
				pq.PushState(State{newCost, newPos})
			}
		})

	}

	return -1
}
