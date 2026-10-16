type BinaryIndexTree struct {
	size         int
	tree1, tree2 []int
}

func NewBinaryIndexTree(size int) *BinaryIndexTree {
	return &BinaryIndexTree{
		size:  size,
		tree1: make([]int, size+1),
		tree2: make([]int, size+1),
	}
}

func (t *BinaryIndexTree) Add(left, right, delta int) {
	t.add(left, delta)     // start applying delta
	t.add(right+1, -delta) // cancel applying delta exclusive
}

func (t *BinaryIndexTree) Query(left, right int) int {
	return t.query(right) - t.query(left-1)
}

func (T *BinaryIndexTree) lowbit(index int) int {
	return index & -index
}

func (t *BinaryIndexTree) add(index, delta int) {
	value := index * delta
	index++

	for index <= t.size {
		t.tree1[index] += delta
		t.tree2[index] += value

		index += t.lowbit(index)
	}
}

func (t *BinaryIndexTree) query(index int) int {
	res := 0
	index++
	mul := index

	for index > 0 {
		res += mul*t.tree1[index] - t.tree2[index]

		index -= t.lowbit(index)
	}

	return res
}

func sumCounts(nums []int) int {
	const (
		MOD = int(1e9) + 7
	)

	n := len(nums)
	res := 0
  cur := 0
	seen := make(map[int]int) // previous number position
	bit := NewBinaryIndexTree(n + 1)

	for i, x := range nums {
		prev, ok := seen[x]
		if !ok {
			prev = -1
		}

		j := prev + 1

    q := bit.Query(j, i)
    cur = (cur + 2 * q + i - j + 1) % MOD
    res = (res + cur) % MOD

    bit.Add(j, i, 1)
    seen[x] = i
	}

	return res
}