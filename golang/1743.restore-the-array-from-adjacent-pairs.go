func dfs(start int, vis map[int]bool, adj map[int][]int, fn func(int)) {
    vis[start] = true
    st := make([]int, 0)
    st = append(st, start)

    for len(st) > 0 {
        node := st[len(st) - 1] // top
        st = st[:len(st) - 1] // pop

        fn(node)

        for _, child := range adj[node] {
            if vis[child] {
                continue
            }
            vis[child] = true
            st = append(st, child)
        }
    }
}

func Reverse(input []int) {
    for i, j := 0, len(input)-1; i < j; i, j = i + 1, j - 1 {
        input[i], input[j] = input[j], input[i]
    }
}

func restoreArray(adjacentPairs [][]int) []int {
    // build adjacency lists
    adj := make(map[int][]int)
    for _, edge := range adjacentPairs {
        adj[edge[0]] = append(adj[edge[0]], edge[1])
        adj[edge[1]] = append(adj[edge[1]], edge[0])
    }
    // get random edge vertices as start 1 and 2
    start1, start2 := adjacentPairs[0][0], adjacentPairs[0][1]

    // visited vertices map
    vis := make(map[int]bool)
    vis[start1] = true
    vis[start2] = true

    // result list
    res1, res2 := make([]int, 0), make([]int, 0)
    // dfs from start1 collecting res to the front
    dfs(start1, vis, adj, func (node int) {
        res1 = append(res1, node)
    })

    // dfs from start2 collecting res to the back
    dfs(start2, vis, adj, func (node int) {
        res2 = append(res2, node)
    })

    Reverse(res2)

    return append(res2, res1...)
}