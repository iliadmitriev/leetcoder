func findCriticalAndPseudoCriticalEdges(n int, edges [][]int) [][]int {
    // append indexes to all edges
    for i := range edges { edges[i] = append(edges[i], i) }
    // sort edges by weight ascending
    sort.Slice(edges, func(i, j int) bool { return edges[i][2] < edges[j][2] })
    
    // answers
    critical, pseudo := []int{}, []int{}
    // Reusable DSU object
    dsu := NewDSU(n)
    // find base minimal weight of MST
    mstWeight := findMSTWeight(edges, nil, nil, &dsu)

    for _, edge := range edges {
        idx := edge[3]

        // find weight with current edge skipped 
        currWeight := findMSTWeight(edges, nil, idx, &dsu)

        // if total weight of MST is greater
        // or graph is disconnected
        // (unable to create MST without current i-th edge)
        // then edge it's critical
        if currWeight > mstWeight || dsu.isles > 1 {
            critical = append(critical, idx)
            continue
        } 
        
        // try to find alternative MST with the same minimal weight
        // having current edge pre-added to MST forcely
        if findMSTWeight(edges, edge, nil, &dsu) == mstWeight {
            pseudo = append(pseudo, idx)
        }
    }

    return [][]int{ critical, pseudo }
}

/////////////////////////
// Kruskal's algorithm //
/////////////////////////
func findMSTWeight(edges [][]int, forcedEdge []int, skip interface{}, dsu *DSU) int {
    dsu.Reset()  // reset reusable DSU
    mstWeight := 0 // result accumulator

    skipIdx, ok := skip.(int)
    if !ok {
        skipIdx = -1
    }

    if forcedEdge != nil { // if forced edge is specified (edge that should be added from the start)
        dsu.Union(forcedEdge[0], forcedEdge[1]) // add edge to DSU (connect components)
        mstWeight += forcedEdge[2] // add edge weight to result
    }

    for _, edge := range edges {
        u, v, weight, i := edge[0], edge[1], edge[2], edge[3]
        // if current edge is not forced edge
        // and can connect 2 components with it
        if i != skipIdx && dsu.Union(u, v) { 
            mstWeight += weight // add it's weight to MST
        }
    }

    return mstWeight
}


//////////////////////////////////////////////////////////////
// DSU Algoritm (iterative, with path compression and rank) //
//////////////////////////////////////////////////////////////
type DSU struct {
    parent, rank []int
    n, isles int
}

func NewDSU(n int) DSU {
    dsu := DSU{make([]int, n), make([]int, n), n, n}
    dsu.Reset()
    return dsu
}

func (dsu *DSU) Reset() {
    dsu.isles = dsu.n
    for i := range dsu.parent {
        dsu.parent[i] = i
        dsu.rank[i] = 1
    }
}

func (dsu *DSU) Find(x int) int {
    for x != dsu.parent[x] {
        dsu.parent[x] = dsu.parent[dsu.parent[x]]
        x = dsu.parent[x]
    }
    return x
}

func (dsu *DSU) Union(v1, v2 int) bool {
    p1, p2 := dsu.Find(v1), dsu.Find(v2)
    if p1 == p2 {
        return false
    }
    // choose lowest rank component 
    // to be merged to largest rank component
    if dsu.rank[p1] > dsu.rank[p2] {
        p1, p2 = p2, p1
    }
    dsu.parent[p1] = dsu.parent[p2] // merge
    dsu.rank[p2] += dsu.rank[p1] // add rank of p1 to p2
    dsu.rank[p1] = 0 // reset rank of p1
    dsu.isles-- // descrease number of islands
    return true
}