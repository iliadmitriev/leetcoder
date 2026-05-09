
type UnionFind struct {
	size       int
	components int
	parent     []int
	rank       []int
}

func NewUnionFind(n int) *UnionFind {
	parent := make([]int, n)
	rank := make([]int, n)
	for i := range parent {
		parent[i] = i
		rank[i] = 1
	}

	return &UnionFind{size: n, components: n, parent: parent, rank: rank}
}

func (uf *UnionFind) find(x int) int {
	for x != uf.parent[x] {
		uf.parent[x] = uf.parent[uf.parent[x]]
		x = uf.parent[x]
	}

	return x
}

func (uf *UnionFind) union(x, y int) bool {
	parX, parY := uf.find(x), uf.find(y)

	if parX == parY {
		return false
	}

	if uf.rank[parX] > uf.rank[parY] {
		parX, parY = parY, parX
	}

	uf.parent[parX] = parY
	uf.rank[parY] += uf.rank[parX]
	uf.rank[parX] = 0
	uf.components--
	return true
}

func (uf *UnionFind) dec() {
	uf.components--
}

func (uf *UnionFind) count() int {
	return uf.components
}

func idx(n, r, c int) int {
	return r*n + c
}

func cross(row, col, m, n int, grid []int, uf *UnionFind) {
	target := m * n

	for r := row - 1; r >= 0; r-- {
		if grid[idx(n, r, col)] == 1 {
			break
		}
		uf.union(idx(n, r, col), target)
	}

	for r := row + 1; r < m; r++ {
		if grid[idx(n, r, col)] == 1 {
			break
		}
		uf.union(idx(n, r, col), target)
	}

	for c := col - 1; c >= 0; c-- {
		if grid[idx(n, row, c)] == 1 {
			break
		}
		uf.union(idx(n, row, c), target)
	}

	for c := col + 1; c < n; c++ {
		if grid[idx(n, row, c)] == 1 {
			break
		}
		uf.union(idx(n, row, c), target)
	}
}

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	grid := make([]int, m*n)
	uf := NewUnionFind(m*n + 1)

	for _, g := range guards {
		grid[idx(n, g[0], g[1])] = 1
		uf.dec()
	}

	for _, w := range walls {
		grid[idx(n, w[0], w[1])] = 1
		uf.dec()
	}

	for _, g := range guards {
		cross(g[0], g[1], m, n, grid, uf)
	}

	return uf.count() - 1
}
