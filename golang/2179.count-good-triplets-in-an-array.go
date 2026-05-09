type FenwickTree struct {
	data []int
}

func NewFenwickTree(n int) *FenwickTree {
	data := make([]int, n+1)
	return &FenwickTree{data: data}
}

// Add v to index i, and all of its ancestors in Fenwick tree
func (f *FenwickTree) Add(i, v int) {
	i++
	for i < len(f.data) {
		f.data[i] += v
		i += i & -i
	}
}

// Sum of values in range [0, i]
func (f *FenwickTree) Sum(i int) int {
	i++
	res := 0
	for i > 0 {
		res += f.data[i]
		i -= i & -i
	}
	return res
}

func goodTriplets(nums1 []int, nums2 []int) int64 {
	n := len(nums1)
	pos2 := make([]int, n)
	reverseIndexes := make([]int, n)
	count := 0

	for i := range n {
		pos2[nums2[i]] = i
	}

	for i := range n {
		reverseIndexes[pos2[nums1[i]]] = i
	}

	fenwick := NewFenwickTree(n)
	for i := range n {
		pos := reverseIndexes[i]
		left := fenwick.Sum(pos)
		fenwick.Add(pos, 1)

		right := n - 1 - pos - (i - left)
		count += left * right
	}

	return int64(count)
}
