import (
    "sort"
)

type DSU struct {
    size int
    parent []int
    rank []int
}

func NewDSU(size int) *DSU {
    parent := make([]int, size)
    rank := make([]int, size)

    for i := range parent {
        rank[i] = 1
        parent[i] = i
    }

    return &DSU{
        size,
        parent,
        rank,
    }
}

func (d *DSU) find(x int) int {
    for x != d.parent[x] {
        d.parent[x] = d.parent[d.parent[x]]
        x = d.parent[x]
    }
    return x
}

func (d *DSU) join(x, y int) bool {
    par_x, par_y := d.find(x), d.find(y)

    if par_x == par_y {
        return false
    }

    if d.rank[par_y] > d.rank[par_x] {
        par_x, par_y = par_y, par_x
    }

    d.parent[par_y] = par_x
    d.rank[par_x] += d.rank[par_y]
    d.rank[par_y] = 0
    return true
}

func (d *DSU) connected(x, y int) bool {
    return d.find(x) == d.find(y)
}

func distanceLimitedPathsExist(n int, edgeList [][]int, queries [][]int) []bool {
    // sort edge list (u, v, dist) by their distance ascending
    sort.Slice(edgeList, func(i, j int) bool {
        return edgeList[i][2] < edgeList[j][2]
    })
    // sort queries (from, to, limit) -> (from, to, limit, index) by limit
    for i := range queries { queries[i] = append(queries[i], i) }
    sort.Slice(queries, func(i, j int) bool {
        return queries[i][2] < queries[j][2]
    })

    // init disjoin set union
    dsu := NewDSU(n)
    edgeIndex := 0
    res := make([]bool, len(queries))

    for _, q := range queries {
        
        for edgeIndex < len(edgeList) && edgeList[edgeIndex][2] < q[2] {
            u, v := edgeList[edgeIndex][0], edgeList[edgeIndex][1]
            dsu.join(u, v)
            edgeIndex++
        }

        res[q[3]] = dsu.connected(q[0], q[1])
    }

    return res
}