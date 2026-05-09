
type UF struct {
	par []int
	w   []int
}

func NewUF(n int) *UF {
	par := make([]int, n)
	w := make([]int, n)
	for i := range par {
		par[i] = i
	}
	return &UF{par: par, w: w}
}

func (u *UF) SetWeights(weights [][]int) {
	m, n := len(weights), len(weights[0])

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			u.w[i*n+j] = weights[i][j]
		}
	}
}

func (u *UF) Find(x int) int {
	for u.par[x] != x {
		u.par[x] = u.par[u.par[x]]
		x = u.par[x]
	}
	return u.par[x]
}

func (u *UF) Union(x, y int) {
	parX, parY := u.Find(x), u.Find(y)
	if parX == parY {
		return
	}

	if u.w[parX] > u.w[parY] {
		parX, parY = parY, parX
	}

	u.par[parX] = parY
	u.w[parY] += u.w[parX]
	u.w[parX] = 0
}

func findMaxFish(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	total := m * n
	maxComponentWeight := 0
	dr, dc := [4]int{0, 0, 1, -1}, [4]int{1, -1, 0, 0}
	uf := NewUF(total)

	uf.SetWeights(grid)

	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] == 0 {
				continue
			}

			idx := r*n + c
			for k := 0; k < 4; k++ {
				nr, nc := r+dr[k], c+dc[k]
				if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0 {
					continue
				}

				nidx := nr*n + nc
				uf.Union(idx, nidx)
			}
		}
	}

	for i := 0; i < total; i++ {
		if uf.Find(i) == i {
			maxComponentWeight = max(maxComponentWeight, uf.w[i])
		}
	}

	return maxComponentWeight
}
