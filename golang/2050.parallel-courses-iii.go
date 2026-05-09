func minimumTime(n int, relations [][]int, time []int) int {
    // build inorder slice
    // build graph adjacency list (shifting vectices numeration to start from 0, not 1)
    inorder := make([]int, n)
    graph := make(map[int][]int)
    for _, rel := range relations {
        inorder[rel[1] - 1]++
        graph[rel[0] - 1] = append(graph[rel[0] - 1], rel[1] - 1)
    }
    // collect all vertices with inorder == 0
    // init endtime vector with their time
    // and add them to queue
    endtime := make([]int, n)
    que := make([]int, 0, n) // start len == 0, but reserve capacity n
    for i := 0; i < n; i++ {
        if inorder[i] == 0 {
            que = append(que, i)
            endtime[i] = time[i]
        }
    }
    res := 0
    // start BFS from those vertices
    for len(que) > 0 {
        node := que[0]
        que = que[1:]
        // chech if it's max endtime
        if res < endtime[node] {
            res = endtime[node]
        }

        for _, child := range graph[node] {
            inorder[child]--
            if inorder[child] == 0 {
                que = append(que, child)
            }
            // update endtime for each vertice to max
            if endtime[child] < endtime[node] + time[child] {
                endtime[child] = endtime[node] + time[child]
            } 
        }
    }
    // return max entime
    return res
}