import (
	"math/bits"
)

/*
Binary Lift Tree (Uplift)
*/
type BinaryLiftTree struct {
	size    int
	logSize int
	depth   []int
	adj     [][]int
	up      [][]int
}

func NewBinaryLiftTree(size int) *BinaryLiftTree {
	logSize := bits.Len(uint(size)) // S:O(1)
	depth := make([]int, size)      // S:O(n)
	adj := make([][]int, size)      // S:O(n)
	up := make([][]int, size)       // S:O(n log(n))

  // T: O(n log(n))
	for i := range size {
		up[i] = make([]int, logSize)
		for j := range logSize {
			up[i][j] = -1
		}
	}

	return &BinaryLiftTree{
		size:    size,
		logSize: logSize,
		adj:     adj,
		depth:   depth,
		up:      up,
	}
}

func (t *BinaryLiftTree) AddEdge(u, v int) {
	if u > v {
		u, v = v, u
	}

	t.adj[u] = append(t.adj[u], v)
}

// T: O(n log(n))
func (t *BinaryLiftTree) Preprocess(root int) {
	t.dfs(root, -1, 0) // root node, parent node of root, initial depth
}

// dfs with each node preprocessing, T: O(n log(n))
func (t *BinaryLiftTree) dfs(u, p, d int) {
	t.depth[u] = d // set node u depth
	t.up[u][0] = p // set node (2^0)-th parent

  // O(log(n))
	for j := 1; j < t.logSize; j++ {
		if t.up[u][j-1] != -1 {
			w := t.up[u][j-1]         // half step up from u to w
			t.up[u][j] = t.up[w][j-1] // half step up from w to p
		} else {
			break
			// t.up[u][j] =-1
		}
	}

	for _, v := range t.adj[u] {
		if v == p { // do not step up back,
			continue
		}

		t.dfs(v, u, d+1) // go to child nodes with depth + 1
	}
}

// kthAncestor finds and returns k-th ancestor of node u
// lift by k nodes with log complexity
// if k == 0 returns node itself
func (t *BinaryLiftTree) kthAncestor(u, k int) int {
	for j := range t.logSize {
		if (k>>j)&1 == 1 {
			u = t.up[u][j]
		}
		if u == -1 {
			return u
		}
	}

	return u
}

// lowes common ancestor of u and v
// check nodes depth, choose which one is deeper
// calculate difference, lift node up using difference
// to make nodes on the same level
// case 1: these nodes is the same single node
// case 2: nodes are different,
// lift both nodes simultaneously until they point to the same node
func (t *BinaryLiftTree) LCA(u, v int) int {
	if t.depth[u] < t.depth[v] {
		u, v = v, u
	}

	u = t.kthAncestor(u, t.depth[u]-t.depth[v])

	if u == v {
		return u
	}

	// try largest step first
	for j := t.logSize - 1; j >= 0; j-- {
		if t.up[u][j] != t.up[v][j] {
			u = t.up[u][j]
			v = t.up[v][j]
		}
	}

	return t.up[u][0]
}

// distance[u, v] = depth[u] + depth[v] - 2 * depth[lca[u, v]]
func (t *BinaryLiftTree) GetDistance(u, v int) int {
	common := t.LCA(u, v)

	return t.depth[u] + t.depth[v] - 2*t.depth[common]
}

const MOD = int(1e9) + 7

func binaryModularExponent(exp int) int {
	res := 1
	base := 2

	for ; exp > 0; exp >>= 1 {
		if exp&1 == 1 {
			res *= base
			res %= MOD
		}

		base *= base
		base %= MOD
	}

	return res
}

func assignEdgeWeights(edges [][]int, queries [][]int) []int {
	n := len(edges) + 1
	bt := NewBinaryLiftTree(n)

	for _, e := range edges {
		bt.AddEdge(e[0]-1, e[1]-1) // add edge with shifted node numeration 1-based to 0-based
	}

	bt.Preprocess(0) // root node

	res := make([]int, len(queries))

	for i, q := range queries {
		dist := bt.GetDistance(q[0]-1, q[1]-1)
		// number of valid combination of length k from {1,2} that sum up to odd number
		// is equal to half of all combiantions
		if dist > 0 {
			res[i] = binaryModularExponent(dist - 1)
		}
	}

	return res
}