import (
    "math"
    "container/heap"
)

type Graph struct {
    size int
    adj map[int][][2]int
}


func Constructor(n int, edges [][]int) Graph {
    adj := make(map[int][][2]int)
    for _, edge := range edges {
        adj[edge[0]] = append(adj[edge[0]], [2]int{edge[1], edge[2]})
    }
    return Graph{ n, adj }
}


func (this *Graph) AddEdge(edge []int)  {
    this.adj[edge[0]] = append(this.adj[edge[0]], [2]int{edge[1], edge[2]})
}


func (this *Graph) ShortestPath(node1 int, node2 int) int {
    // init distances as infinity, and mark start vertice distance as 0
    dist := make([]int, this.size)
    for i := range dist {
        dist[i] = math.MaxInt
    }
    dist[node1] = 0
    // init priority queue (min heap) of (distance, node) tuples
    // with reserved size
    // push start node to it
    pq := make(MinHeap, 0, this.size)
    heap.Push(&pq, [2]int{0, node1})

    for pq.Len() > 0 {
        top := heap.Pop(&pq).([2]int)
        distance, node := top[0], top[1]

        if node == node2 {
            return distance
        }

        if distance > dist[node] {
            continue
        }

        for _, next := range this.adj[node] {
            child, cost := next[0], next[1]
            if dist[child] <= distance + cost {
                continue
            }

            dist[child] = distance + cost
            heap.Push(&pq, [2]int{distance + cost, child})
        }
    }
    return -1
}


type MinHeap [][2]int

// Len, Less, Swap
func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i][0] < h[j][0] }
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
// Pop, Push
func (h *MinHeap) Push(x interface{}) {
    *h = append(*h, x.([2]int))
}
func (h *MinHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[:n - 1]
    return x
}