type UnionFindComp struct {
	comp                int
	n                   int
	vert, parent, edges []int
}

func NewUnionFindComp(n int) *UnionFindComp {
	vert := make([]int, n)
	parent := make([]int, n)
	edges := make([]int, n)

	for i := range n {
		vert[i] = 1
		parent[i] = i
	}

	return &UnionFindComp{
		comp:   n,
		n:      n,
		edges:  edges,
		parent: parent,
		vert:   vert,
	}
}

func (u *UnionFindComp) find(x int) int {
	for x != u.parent[x] {
		u.parent[x] = u.parent[u.parent[x]]
		x = u.parent[x]
	}
	return x
}

func (u *UnionFindComp) join(x1, x2 int) {
	if x1 == x2 {
		return
	}

	p1, p2 := u.find(x1), u.find(x2)

	if p1 == p2 {
		u.edges[p2]++
		return
	}

	u.comp--
	u.parent[p1] = p2
	u.vert[p2] += u.vert[p1]
	u.edges[p2] += u.edges[p1] + 1
}

func (u *UnionFindComp) get() [][2]int {
	res := make([][2]int, 0, u.comp)
	seen := make(map[int]bool, u.n)

	for i := range u.n {
		p := u.find(i)

		if seen[p] {
			continue
		}

		res = append(res, [2]int{u.vert[p], u.edges[p]})
		seen[p] = true
	}

	return res
}

func countCompleteComponents(n int, edges [][]int) int {
	uf := NewUnionFindComp(n)
	count := 0

	for _, e := range edges {
		uf.join(e[0], e[1])
	}

	for _, c := range uf.get() {
		if c[1] == c[0]*(c[0]-1)/2 {
			count++
		}
	}

	return count
}
