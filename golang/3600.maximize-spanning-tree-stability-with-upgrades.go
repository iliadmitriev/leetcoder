type DSU struct {
	parent []int
}

// NewDSUWithParent creates new DSU data stucture by copying parent connection of existing one.
func NewDSUWithParent(other *DSU) *DSU {
	n := len(other.parent)
	parent := make([]int, n)
	copy(parent, other.parent)

	return &DSU{
		parent: parent,
	}
}

// NewDSU create new DSU data structure from scratch with initialization.
func NewDSU(n int) *DSU {
	par := make([]int, n)
	for i := range par {
		par[i] = i
	}

	return &DSU{
		parent: par,
	}
}

// find returns node x parent, returns x if it's a component root node.
func (d *DSU) find(x int) int {
	for x != d.parent[x] {
		d.parent[x] = d.parent[d.parent[x]] // path compression
		x = d.parent[x]
	}

	return x
}

// join joins two nodes (y and y) to component and return success; otherwise if nodes already connected return false.
func (d *DSU) join(x, y int) bool {
	px, py := d.find(x), d.find(y)
	if px == py {
		return false // already connected, there is no need to join
	}

	d.parent[px] = py
	return true // successfull join
}

func maxStability(n int, edges [][]int, k int) int {
	m := len(edges) // edges[from, to, weight, required]

	if m < n-1 {
		return -1 // optimization 1: there is no way to connect n nodes with less than n - 1 edges.
	}

	must, optional := [][]int{}, [][]int{}

	for _, e := range edges {
		if e[3] == 1 {
			must = append(must, e)
		} else {
			optional = append(optional, e)
		}
	}

	if len(must) > n-1 {
		return -1 // optimization 2: if we have to use more than n - 1 edges to connect n nodes,
		// there definatelly will be a cycle introduced.
	}

	// try to add all the required edges to base DSU data structure:
	// 1. calculate minimal stability
	// 2. calcualte base component size
	// 3. early return if there is cycle introduced or reached edge limit
	dsuBase := NewDSU(n)
	selectedBase := 0

	// max minimal stability is 10^5
	minStability := int(1e6) * 2

	for _, e := range must {
		u, v, w := e[0], e[1], e[2]
		// if required edge introduces a cycle or
		// number of reuiqred edges in the component is n - 1
		// there is no solution
		if !dsuBase.join(u, v) || selectedBase == n-1 {
			return -1
		}

		selectedBase++
		minStability = min(minStability, w)
	}

	// === kruskal's algorithm:
	// 1. sort edges by weight
	// 2. iterate over edges and add to component (if it doesn't introduce cycle, is not already connected)
	// 3. if component length is reached minimal spanning tree size then brake

	sort.Slice(optional, func(i, j int) bool {
		return optional[i][2] > optional[j][2]
	})

	res := -1 // by default the answer hasn't been found yet
	lo, hi := 0, minStability // inclusive range to find the answer

	// use binary search to find appropriate best solution (can be multiple)
	for lo < hi {
		mid := lo + (hi-lo+1)/2

		dsu := NewDSUWithParent(dsuBase)
		selected := selectedBase
		double := 0 // doubled edges count

		for _, e := range optional {
			u, v, w := e[0], e[1], e[2]

			if dsu.find(u) == dsu.find(v) {
				continue
			}

			if w >= mid { // if weight if greater or eq to the limit
				_ = dsu.join(u, v)
				selected++
			} else if double < k && w*2 >= mid { // if weight less but can be reached limit by doubling
				double++
				_ = dsu.join(u, v)
				selected++
			} else { // no need to go further, all the next optional edges in sorted list will be with less weight
				break
			}

      // break the search: one of the answers is found
			if selected == n-1 {
				break
			}
		}

		// choose step
		if selected != n-1 {
			hi = mid - 1
		} else {
			res = mid
			lo = mid
		}
	}

	return res
}