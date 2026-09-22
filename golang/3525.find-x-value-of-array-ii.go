const MAXK = 6

type SegmentTree struct {
	n, k int
	tree [][MAXK]int
}

func NewSegmentTree(arr []int, k int) *SegmentTree {
	n := len(arr)
	size := 2 << int(math.Ceil(math.Log2(float64(n))))
	tree := make([][MAXK]int, size)

	seg := &SegmentTree{
		k:    k,
		n:    n,
		tree: tree,
	}

	seg.build(arr, 1, 0, n-1)

	return seg
}

func (t *SegmentTree) build(arr []int, o, l, r int) {
	if l == r {
		t.makeNode(o, arr[l])
		return
	}

	m := (l + r) / 2
	t.build(arr, o*2, l, m)
	t.build(arr, o*2+1, m+1, r)

	t.mergeNode(&t.tree[o*2], &t.tree[o*2+1], &t.tree[o])
}

func (t *SegmentTree) makeNode(o, value int) {
	for i := range MAXK {
		t.tree[o][i] = 0
	}

	k := t.k
	r := value % k
	t.tree[o][r] = 1
	t.tree[o][k] = r
}

func (t *SegmentTree) mergeNode(left, right, res *[MAXK]int) {
	for i := range MAXK {
		(*res)[i] = 0
	}

	k := t.k
	mul_L := (*left)[k]
	mul_R := (*right)[k]
	(*res)[k] = (mul_L * mul_R) % k

	for x := range k {
		(*res)[x] = (*left)[x]
	}

	for x := range k {
		(*res)[(mul_L*x)%k] += (*right)[x]
	}
}

func (t *SegmentTree) update(o, l, r, index, value int) {
	if l == r {
		t.makeNode(o, value)
    return
	}

	m := (l + r) / 2
	if index <= m {
		t.update(o*2, l, m, index, value)
	} else {
		t.update(o*2+1, m+1, r, index, value)
	}

	t.mergeNode(&t.tree[o*2], &t.tree[o*2+1], &t.tree[o])
}

func (t *SegmentTree) query(o, l, r, L, R int) [MAXK]int {
	// if request [L,R] spans over both node's children
	if L <= l && r <= R {
		return t.tree[o]
	}

	m := (l + r) / 2
	// if request [L,R] spans only over node's the left child
	if R <= m {
		return t.query(o*2, l, m, L, R)
	}
	// if request [L,R] spans only over node's right child
	if L > m {
		return t.query(o*2+1, m+1, r, L, R)
	}

	left := t.query(o*2, l, m, L, R)
	right := t.query(o*2+1, m+1, r, L, R)
	res := [MAXK]int{}

	t.mergeNode(&left, &right, &res)

	return res
}

func (t *SegmentTree) Update(index, value int) {
	t.update(1, 0, t.n-1, index, value)
}

func (t *SegmentTree) Query(L, R int) [MAXK]int {
	return t.query(1, 0, t.n-1, L, R)
}

func resultArray(nums []int, k int, queries [][]int) []int {
	n := len(nums)
  seg := NewSegmentTree(nums, k)
	result := make([]int, len(queries))

	for i, q := range queries {
		index, value, start, x := q[0], q[1], q[2], q[3]

		seg.Update(index, value)
		res := seg.Query(start, n-1)
		result[i] = res[x]
	}

	return result
}