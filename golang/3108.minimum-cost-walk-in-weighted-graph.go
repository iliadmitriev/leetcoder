type UnionFindAND struct {
	parent []int
	weight []int
}

func NewUnionFindAND(n int) *UnionFindAND {
	p := make([]int, n)
	w := make([]int, n)
	for i := range p {
		p[i] = i
		w[i] = -1
	}
	return &UnionFindAND{parent: p, weight: w}
}

func (u *UnionFindAND) Find(x int) (int, int) {
	for x != u.parent[x] {
		u.weight[x] &= u.weight[u.parent[x]]
		u.weight[u.parent[x]] &= u.weight[x]

		u.parent[x] = u.parent[u.parent[x]]
		x = u.parent[x]

	}

	return x, u.weight[x]
}

func (u *UnionFindAND) Union(x1, x2, w int) {
	p1, w1 := u.Find(x1)
	p2, w2 := u.Find(x2)

	w &= w1 & w2
	u.parent[p1] = p2
	u.weight[p1] = w
	u.weight[p2] = w
}

func minimumCost(n int, edges [][]int, query [][]int) []int {
	uf := NewUnionFindAND(n)
	res := make([]int, len(query))
	for _, e := range edges {
		uf.Union(e[0], e[1], e[2])
	}

	for i, q := range query {
		res[i] = -1

		if q[0] == q[1] {
			continue
		}

		p1, w1 := uf.Find(q[0])
		p2, w2 := uf.Find(q[1])

		if p1 != p2 {
			continue
		}

		res[i] = w1 & w2
	}

	return res
}
