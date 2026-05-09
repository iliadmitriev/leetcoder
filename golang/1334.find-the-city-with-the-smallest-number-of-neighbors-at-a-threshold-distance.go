
import (
	"container/heap"
	"math"
)

func findTheCity(n int, edges [][]int, distanceThreshold int) int {
	adj := make([][][2]int, n)
	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], [2]int{e[2], e[1]})
		adj[e[1]] = append(adj[e[1]], [2]int{e[2], e[0]})
	}

	target, minCount := -1, math.MaxInt32
	for i := 0; i < n; i++ {
		count := dijkstraWithThreshouldCount(i, n, distanceThreshold, adj)
		if count <= minCount {
			minCount = count
			target = i
		}
	}

	return target
}

func dijkstraWithThreshouldCount(src, n, threshold int, adj [][][2]int) int {
	hq := MinHeap(make([][2]int, 0, n))
	heap.Push(&hq, [2]int{0, src})
	dist := make([]int, n)
	for i := range dist {
		dist[i] = math.MaxInt32
	}
	dist[src] = 0

	for len(hq) > 0 {
		u := heap.Pop(&hq).([2]int)
		if u[0] > threshold {
			continue
		}

		for _, v := range adj[u[1]] {
			if u[0]+v[0] >= dist[v[1]] {
				continue
			}
			heap.Push(&hq, [2]int{u[0] + v[0], v[1]})
			dist[v[1]] = u[0] + v[0]
		}
	}
	dist[src] = math.MaxInt32

	count := 0
	for _, d := range dist {
		if d <= threshold {
			count++
		}
	}

	return count
}

type MinHeap [][2]int

func (h MinHeap) Len() int            { return len(h) }
func (h MinHeap) Less(i, j int) bool  { return h[i][0] < h[j][0] }
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.([2]int)) }
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
