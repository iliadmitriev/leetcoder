type DSU struct {
	size   int
	parent []int
	rank   []int
}

func NewDSU(size int) *DSU {
	rank := make([]int, size)
	parent := make([]int, size)
	for i := 0; i < size; i++ {
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

func (d *DSU) count() int {
	cache := make([]int, d.size)
	counter := 0
	var par int
	for i := 0; i < d.size; i++ {
		par = d.find(i)
		counter += 1 - cache[par]
		cache[par] = 1
	}
	return counter
}

func maxNumEdgesToRemove(n int, edges [][]int) int {
	bob, alice := NewDSU(n), NewDSU(n)
	bob_edges := make([][2]int, 0, len(edges))
	alice_edges := make([][2]int, 0, len(edges))
	both := make([][2]int, 0, len(edges))

	// sort split edges between 3 slices
	// `edge[1] - 1` - edges numeration starts from 1, but not 0
	for _, edge := range edges {
		if edge[0] == 1 {
			alice_edges = append(alice_edges, [2]int{edge[1] - 1, edge[2] - 1})
		} else if edge[0] == 2 {
			bob_edges = append(bob_edges, [2]int{edge[1] - 1, edge[2] - 1})
		} else {
			both = append(both, [2]int{edge[1] - 1, edge[2] - 1})
		}
	}

	// remove counter
	counter := 0

	for _, edge := range both {
		res1 := bob.join(edge[0], edge[1])
		res2 := alice.join(edge[0], edge[1])

		if !res1 || !res2 {
			counter++
		}
	}

	for _, edge := range alice_edges {
		if !alice.join(edge[0], edge[1]) {
			counter++
		}
	}

	for _, edge := range bob_edges {
		if !bob.join(edge[0], edge[1]) {
			counter++
		}
	}

	if alice.count() == 1 && bob.count() == 1 {
		return counter
	}

	return -1
}
