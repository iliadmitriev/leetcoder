type SegmentTree struct {
	n              int
	buf            []byte
	pre, suf, best []int
}

func NewSegmentTree(s string) *SegmentTree {
	n := len(s)
	buf := []byte(s)

	pre := make([]int, n<<2)
	suf := make([]int, n<<2)
	best := make([]int, n<<2)

	tree := SegmentTree{
		n:    n,
		buf:  buf,
		pre:  pre,
		suf:  suf,
		best: best,
	}

	tree.build(1, 0, n-1)

	return &tree
}

// build tree from current node for the segment [l, r]
func (t *SegmentTree) build(node, l, r int) {
	// base case (single node)
	if l == r {
		t.pre[node] = 1
		t.suf[node] = 1
		t.best[node] = 1

		return
	}

	mid := (l + r) >> 1

	t.build(node<<1, l, mid)
	t.build(node<<1|1, mid+1, r)

	t.updateNode(node, l, r)
}

// updateNode update current single node with it's children values
func (t *SegmentTree) updateNode(node, l, r int) {
	left := node << 1
	right := node<<1 | 1
	// init base (parts do not match)
	t.pre[node] = t.pre[left]
	t.suf[node] = t.suf[right]
	t.best[node] = max(t.best[left], t.best[right])

	mid := (l + r) >> 1

	// if they match
	if t.buf[mid] == t.buf[mid+1] {
		lenL := mid - l + 1
		lenR := r - mid

		if lenL == t.pre[left] {
			t.pre[node] = t.pre[left] + t.pre[right]
		}

		if lenR == t.suf[right] {
			t.suf[node] = t.suf[left] + t.suf[right]
		}

		t.best[node] = max(t.best[node], t.suf[left]+t.pre[right])
	}
}

// update whole tree from node for segment [l, r]
// changing symbol at pos
func (t *SegmentTree) update(node, l, r, pos int) {
	if l == r {
		return
	}

	mid := (l + r) >> 1

	if pos <= mid {
		t.update(node<<1, l, mid, pos)
	} else {
		t.update(node<<1|1, mid+1, r, pos)
	}

	t.updateNode(node, l, r)
}

// UpdateCharAt update char in buffet at position
// and rebuild the tree.
func (t *SegmentTree) UpdateCharAt(ch byte, pos int) {
	t.buf[pos] = ch
	t.update(1, 0, t.n-1, pos)
}

func (t *SegmentTree) GetBest() int {
	return t.best[1]
}

func longestRepeating(s string, queryCharacters string, queryIndices []int) []int {
	k := len(queryCharacters)
	res := make([]int, k)
	tree := NewSegmentTree(s)

	for i := range k {
		tree.UpdateCharAt(queryCharacters[i], queryIndices[i])
		res[i] = tree.GetBest()
	}

	return res
}