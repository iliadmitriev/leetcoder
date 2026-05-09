import (
    "container/heap"
)

type Point struct {
    weight int
    idx int
}

type Points []Point

// len, less and swap methods for container
func (p Points) Len() int { return len(p) }
func (p Points) Less(i, j int) bool { return p[i].weight < p[j].weight }
func (p Points) Swap(i, j int) { p[i], p[j] = p[j], p[i] }

// push to container
func (p *Points) Push(x interface{}) {
    *p = append(*p, x.(Point))
}

// pop from container
func (p *Points) Pop() interface{} {
    old := *p
    n := len(old)
    x := old[n - 1]
    *p = old[0: n - 1]
    return x
}

// Abs returns the absolute value of x.
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// get manhattan distance between two points
func dist(p1, p2 []int) int {
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]);
}

func minCostConnectPoints(points [][]int) int {

    n := len(points)
    // weight, vertice idx heap priority queue
    hq := &Points{ Point{0, 0} }
    heap.Init(hq)
    // all visited vertices
    seen := make([]bool, n)

    // result
    mst := 0
    count := 0

    for count < n {
        point := heap.Pop(hq).(Point)

        if seen[point.idx] {
            continue
        }

        seen[point.idx] = true
        mst += point.weight
        count += 1

        for next := range points {
            if !seen[next] {
                heap.Push(hq, Point{ dist(points[point.idx], points[next]), next })
            }
        }
    }

    return mst
}