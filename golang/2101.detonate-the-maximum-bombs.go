func bfs(start int, graph [][]int) int {
    count := 0
    q := make([]int, 0, len(graph))
    q = append(q, start)
    vis := make([]bool, len(graph))
    vis[start] = true

    for len(q) > 0 {
        node := q[0]
        q = q[1:]
        count++

        for _, g := range graph[node] {
            if !vis[g] {
                vis[g] = true
                q = append(q, g)
            }
        }
    }
    return count
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func pow2(x int) int {
    return x * x
}

func maximumDetonation(bombs [][]int) int {
    // build indegree and directed graph
    // using formula x^2 + x^2 <= r^2
    // sort vertices ascending using indegree
    // iterate vertices using bfs find each component size
    // return max component size
    n := len(bombs)
    // build directed graph and indegree
    indegree := make([]int, n)
    graph := make([][]int, n)
    for i := range graph { graph[i] = make([]int, 0)}
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if i != j && pow2(bombs[i][0] - bombs[j][0]) + pow2(bombs[i][1] - bombs[j][1]) <= pow2(bombs[i][2]) {
                graph[i] = append(graph[i], j)
                indegree[j]++
            }
            if indegree[j] == n - 1 {
                return n
            }
        }
    }
    // sort vertices using indegree
    vertices := make([]int, n)
    for i := 0; i < n; i++ { vertices[i] = i }
    sort.Slice(vertices, func(i, j int) bool { return indegree[i] < indegree[j] })
    // bfs
    count := 0
    for _, v := range vertices {
        count = max(count, bfs(v, graph))
        if count == n {
            return n
        }
    }

    return count
}