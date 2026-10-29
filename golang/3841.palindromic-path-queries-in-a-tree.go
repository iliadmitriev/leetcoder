import (
	"strings"
	"strconv"
	"math/bits"
)

type BinaryIndexTree struct {
	n    int
	tree []int
}

func NewBinaryIndexTree(n int) *BinaryIndexTree {
	return &BinaryIndexTree{
		n:    n,
		tree: make([]int, n+1),
	}
}

func lowbit(i int) int {
	return i & -i
}

func (t *BinaryIndexTree) Query(i int) int {
	res := 0
	for i > 0 {
		res ^= t.tree[i]
		i -= lowbit(i)
	}

	return res
}

func (t *BinaryIndexTree) Update(i, v int) {
	for i <= t.n {
		t.tree[i] ^= v
		i += lowbit(i)
	}
}

func (t *BinaryIndexTree) UpdateRange(l, r, v int) {
	t.Update(l, v)
	t.Update(r+1, v)
}

type BinaryUpliftTree struct {
	n, LOG, t int
	tree      [][]int
	l, r, dep []int // preorder indices, postorder indices, depth
}

func NewBinaryUpliftTree(n int) *BinaryUpliftTree {
	LOG := bits.Len(uint(n))
	tree := make([][]int, n)
	for i := range n {
		tree[i] = make([]int, LOG)
	}

	return &BinaryUpliftTree{
		n:    n,
		LOG:  LOG,
		t:    0,
		tree: tree,
		l:    make([]int, n),
		r:    make([]int, n),
		dep:  make([]int, n),
	}
}

func (t *BinaryUpliftTree) dfs(g [][]int, u, p int) {
	t.t++

	t.l[u] = t.t
	t.tree[u][0] = p

	for _, v := range g[u] {
		if v == p {
			continue
		}

		t.dep[v] = t.dep[u] + 1
		t.dfs(g, v, u)
	}

	t.r[u] = t.t
}

func (t *BinaryUpliftTree) Build(g [][]int) {
	t.dfs(g, 0, 0)

	for j := 1; j < t.LOG; j++ {
		for i := 0; i < t.n; i++ {
			prev := t.tree[i][j-1]
			t.tree[i][j] = t.tree[prev][j-1]
		}
	}
}

func (t *BinaryUpliftTree) LCA(u, v int) int {
	if t.dep[u] < t.dep[v] {
		u, v = v, u
	}

	diff := t.dep[u] - t.dep[v]
	for j := 0; j < t.LOG; j++ {
		if (diff>>j)&1 == 1 {
			u = t.tree[u][j]
		}
	}

	if u == v {
		return u
	}

	for j := t.LOG - 1; j >= 0; j-- {
		if t.tree[u][j] != t.tree[v][j] {
			u = t.tree[u][j]
			v = t.tree[v][j]
		}
	}

	return t.tree[u][0]
}

func (t *BinaryUpliftTree) Left(i int) int {
	return t.l[i]
}

func (t *BinaryUpliftTree) Right(i int) int {
	return t.r[i]
}

func palindromePath(n int, edges [][]int, s string, queries []string) []bool {
	sb := []byte(s) // shadow

	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}

	charBit := func(ch byte) int {
		return 1 << (ch - 'a')
	}

	res := make([]bool, 0)
	bit := NewBinaryIndexTree(n + 1)
	but := NewBinaryUpliftTree(n)

	but.Build(g) // build flat tree from graph

	for i := range n {
		bit.UpdateRange(
			but.Left(i),
			but.Right(i),
			charBit(sb[i]),
		)
	}

	for _, q := range queries {
		fields := strings.Fields(q)

		if fields[0] == "update" {
			u, _ := strconv.Atoi(fields[1])
			ch := fields[2][0]

			bit.UpdateRange(
				but.Left(u),
				but.Right(u),
				charBit(ch)^charBit(sb[u]),
			)
			sb[u] = ch

		} else { // query

			u, _ := strconv.Atoi(fields[1])
			v, _ := strconv.Atoi(fields[2])

			w := but.LCA(u, v)
			mask := bit.Query(but.Left(u)) ^ bit.Query(but.Left(v)) ^ charBit(sb[w])
			res = append(res, mask&(mask-1) == 0)
		}
	}

	return res
}