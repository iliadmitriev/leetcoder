func bfs(start int, vis []bool, gr [][]int) {
    q := make([]int, 0)
    q = append(q, start)
    vis[start] = true

    for len(q) > 0 {
        for m := len(q); m > 0; m-- {
            u := q[0]
            q = q[1:]
            for _, v := range gr[u] {
                if vis[v] {
                    continue
                }
                vis[v] = true
                q = append(q, v)
            }
        }
    }
}

func findCircleNum(isConnected [][]int) int {
    n := len(isConnected)
    gr := make([][]int, n)
    for i := 0; i < n; i++ { gr[i] = make([]int, 0) }

    for u := 0; u < n; u++ {
        for v := u + 1; v < n; v++ {
            if isConnected[u][v] == 1 {
                gr[u] = append(gr[u], v)
                gr[v] = append(gr[v], u)
            }
        }
    }

    vis := make([]bool, n)
    count := 0
    for u := 0; u < n; u++ {
        if vis[u] {
            continue
        }
        bfs(u, vis, gr)
        count++
    }
    return count;
}