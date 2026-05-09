type Node struct {
    node string
    value float64
}

type Graph map[string][]Node

func bfs(start string, end string, graph Graph) float64 {
    if _, ok := graph[start]; !ok {
        return -1.0
    }

    if  _, ok := graph[end]; !ok {
        return -1.0
    }

    que := make([]Node, 0, 40)
    vis := make(map[string]bool)
    que = append(que, Node{start, 1.0})
    vis[start] = true

    for len(que) > 0 {
        node := que[0]
        que = que[1:]

        if node.node == end {
            return node.value
        }

        for _, child := range graph[node.node] {
            if vis[child.node] {
                continue
            }
            que = append(que, Node{ child.node, node.value * child.value })
            vis[child.node] = true
        }
    }

    return -1.0
}

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    graph := make(Graph)
    for i, eq := range equations {
        a, b := eq[0], eq[1]
        graph[a] = append(graph[a], Node{b, values[i]})
        graph[b] = append(graph[b], Node{a, 1.0 / values[i]})
    }

    res := make([]float64, len(queries))
    for i := 0; i < len(queries); i++ {
        res[i] = bfs(queries[i][0], queries[i][1], graph)
    }
    return res
}