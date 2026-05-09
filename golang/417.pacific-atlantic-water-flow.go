var dirs = [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func pacificAtlantic(heights [][]int) [][]int {
	atlantic, pacific := NewIsland(heights), NewIsland(heights)

	rows, cols := len(heights), len(heights[0])

	for r := range rows {
		atlantic.DFS(r, 0)
		pacific.DFS(r, cols-1)
	}

	for c := range cols {
		atlantic.DFS(0, c)
		pacific.DFS(rows-1, c)
	}

	both := make([][]int, 0)

	for r := range rows {
		for c := range cols {
			if pacific.IsVisited(r, c) && atlantic.IsVisited(r, c) {
				both = append(both, []int{r, c})
			}
		}
	}

	return both
}

type Island struct {
	heights    [][]int
	rows, cols int
	vis        [][]bool
}

func NewIsland(heights [][]int) *Island {
	rows, cols := len(heights), len(heights[0])
	vis := make([][]bool, rows)
	for i := range vis {
		vis[i] = make([]bool, cols)
	}

	return &Island{
		heights: heights,
		rows:    rows,
		cols:    cols,
		vis:     vis,
	}
}

func (i *Island) DFS(r, c int) {
	if i.vis[r][c] {
		return
	}

	i.dfs(r, c)
}

func (i *Island) IsVisited(r, c int) bool {
	return i.vis[r][c]
}

func (i *Island) dfs(r, c int) {
	i.vis[r][c] = true

	for _, dir := range dirs {
		nr, nc := r+dir[0], c+dir[1]

		if nr < 0 || nr >= i.rows || nc < 0 || nc >= i.cols {
			continue
		}

		if i.vis[nr][nc] {
			continue
		}

		if i.heights[nr][nc] < i.heights[r][c] {
			continue
		}

		i.vis[nr][nc] = true
		i.dfs(nr, nc)
	}
}
