// returns true if able to color whole component with 2 colors (0 - black, 1 - red, -1 not colored)
// false otherwise
func bfs(node int, graph [][]int, colors []int) bool {
    que := make([]int, 1, len(graph))
    que[0] = node
    colors[node] = 0 // start with black - 0

    for len(que) > 0 {
        node = que[0]
        que = que[1:]

        for _, child := range graph[node] {
            if colors[child] == -1 {
                colors[child] = 1 - colors[node]
                que = append(que, child)
            } else if colors[child] != 1 - colors[node] {
                return false
            }
        }
    }

    return true
}

func isBipartite(graph [][]int) bool {
    colors := make([]int, len(graph))
    for i := range colors { colors[i] = -1 }

    for start := 0; start < len(graph); start++ {
        if colors[start] == -1 && !bfs(start, graph, colors) {
            return false
        }
    }
    return true
}