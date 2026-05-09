
// MaxSegmentTree is a maximum segment tree implementation.
type MaxSegmentTree struct {
	size int
	tree []int
}

func NewMaxSegmentTree(data []int) *MaxSegmentTree {
	n := len(data)
	size := 1

	for size < n {
		size <<= 1
	}

	tree := make([]int, size*2)

	for i, d := range data {
		tree[size+i] = d
	}

	for i := size - 1; i > 0; i-- {
		tree[i] = max(tree[2*i], tree[2*i+1])
	}

	return &MaxSegmentTree{
		size: size,
		tree: tree,
	}
}

func (m *MaxSegmentTree) update(i, x int) {
	i += m.size

	m.tree[i] = x
	i >>= 1

	for i > 0 {
		m.tree[i] = max(m.tree[2*i], m.tree[2*i+1])
		i >>= 1
	}
}

// find retrieves first met element >= x.
func (m *MaxSegmentTree) find(x int) int {
	i := 1

	if x > m.tree[i] {
		return -1
	}

	for i < m.size {
		if m.tree[2*i] >= x {
			i = 2 * i
		} else {
			i = 2*i + 1
		}
	}

	return i - m.size
}

func numOfUnplacedFruits(fruits []int, baskets []int) int {
	tree := NewMaxSegmentTree(baskets)
	count := 0

	for _, fruit := range fruits {
		j := tree.find(fruit)

		if j == -1 {
			count++
			continue
		}

		tree.update(j, 0)
	}

	return count
}
