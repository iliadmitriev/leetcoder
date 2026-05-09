type Point struct {
    y int
    x int
}

type Visited map[Point]bool

type Dist struct {
    p Point
    dist int
}

// find first land cell from one of two islands
func findStart(grid [][]int) Point {
    m, n := len(grid), len(grid[0])
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                return Point{i, j}
            }
        }
    }
    return Point{0, 0}
}

// detect all island cells and walk/mark them
func dfs(start Point, vis Visited, grid [][]int) []Point {
    m, n := len(grid), len(grid[0])
    res := make([]Point, 0, m * n)

    stack := make([]Point, 0, m * n)
    stack = append(stack, start)
    vis[start] = true
    phase := []int{-1, 0, 1, 0, -1}

    for len(stack) > 0 {
        node := stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]
        res = append(res, node)

        for i := 0; i < 4; i++ {
            y, x := node.y + phase[i], node.x + phase[i + 1]
            nxt := Point{ y, x }
            if 0 <= y && y < m && 0 <= x && x < n && !vis[nxt] && grid[y][x] == 1 {
                vis[nxt] = true
                stack = append(stack, nxt)
            }
        }
    }

    return res
}

// start bfs simultaneously from 1st island
func bfs(start []Point, vis Visited, grid [][]int) int {
    m, n := len(grid), len(grid[0])
    queue := make([]Dist, 0, m * n)
    for _, p := range start {
        queue = append(queue, Dist{p, 0})
    }
    phase := []int{-1, 0, 1, 0, -1}

    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]

        for i := 0; i < 4; i++ {
            y, x := node.p.y + phase[i], node.p.x + phase[i + 1]
            nxt := Point{ y, x }
            if 0 <= y && y < m && 0 <= x && x < n && !vis[nxt] {
                if grid[y][x] == 1 {
                    return node.dist
                } else {
                    vis[nxt] = true
                    queue = append(queue, Dist{nxt, node.dist + 1})
                }
            }
        }
    }

    return -1
}

func shortestBridge(grid [][]int) int {

    vis := make(Visited)

    start := findStart(grid)
    island := dfs(start, vis, grid)

    return bfs(island, vis, grid)
}