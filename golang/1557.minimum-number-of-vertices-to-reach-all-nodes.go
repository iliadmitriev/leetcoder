func findSmallestSetOfVertices(n int, edges [][]int) []int {
    indegree := make([]bool, n)
    for _, edge := range edges {
        indegree[edge[1]] = true
    }
    res := make([]int, 0)
    for i := 0; i < n; i++ {
        if !indegree[i] {
            res = append(res, i)
        }
    }
    return res
}