package main

import "slices"

// SegTree implements a segment tree for range maximum queries with point updates.
// Each node stores the maximum value in its range, enabling O(log N) queries and updates.
type SegTree struct {
	n    int   // number of leaves (padded to power of 2)
	tree []int // tree[1] is root, tree[2*i] and tree[2*i+1] are children
}

// NewSegTree creates a segment tree for range [0, size] inclusive.
// size: maximum coordinate value that can be queried.
func NewSegTree(size int) *SegTree {
	// Pad to next power of 2 for complete binary tree
	n := 1
	for n <= size {
		n <<= 1
	}
	return &SegTree{
		n:    n,
		tree: make([]int, 2*n),
	}
}

// Update sets value at position idx to val and propagates changes upward.
// idx: 0-based position; val: new value to store.
// Complexity: O(log N).
func (s *SegTree) Update(idx, val int) {
	// Convert to leaf index in tree array
	pos := idx + s.n
	s.tree[pos] = val
	// Bubble up to update ancestors
	for pos >>= 1; pos >= 1; pos >>= 1 {
		s.tree[pos] = max(s.tree[2*pos], s.tree[2*pos+1])
	}
}

// Query returns maximum value in range [l, r] inclusive (0-based).
// l, r: range boundaries; returns 0 if l > r.
// Complexity: O(log N).
func (s *SegTree) Query(l, r int) int {
	if l > r {
		return 0
	}
	// Convert to leaf indices
	l += s.n
	r += s.n
	mx := 0

	for l <= r {
		// If l is right child, include it and move to next sibling
		if l&1 == 1 {
			mx = max(mx, s.tree[l])
			l++
		}
		// If r is left child, include it and move to previous sibling
		if r&1 == 0 {
			mx = max(mx, s.tree[r])
			r--
		}
		// Move to parent level
		l >>= 1
		r >>= 1
	}

	return mx
}

func handleType1(x int, obs []int, seg *SegTree) []int {
	idx, _ := slices.BinarySearch(obs, x)
	prev, next := obs[idx-1], obs[idx]

	// Update gaps: split (next-prev) into (x-prev) at x and (next-x) at next
	seg.Update(x, x-prev)
	seg.Update(next, next-x)

	return slices.Insert(obs, idx, x)
}

func handleType2(x, sz int, obs []int, seg *SegTree) bool {
	idx, _ := slices.BinarySearch(obs, x)
	if idx == len(obs) || obs[idx] != x {
		idx--
	}
	lastObs := obs[idx]

	// Max gap is either: stored gap ending in [0,x], or trailing gap to x
	maxGap := max(seg.Query(0, x), x-lastObs)

	return maxGap >= sz
}

func getResults(queries [][]int) []bool {
	maxX := slices.MaxFunc(queries, func(a, b []int) int {
		return cmp.Compare(a[1], b[1])
	})[1]

	// Initialize with sentinel obstacles at 0 and maxX+1
	obs := []int{0, maxX + 1}
	seg := NewSegTree(maxX + 2)
	seg.Update(maxX+1, maxX+1) // initial gap spans entire range

	results := make([]bool, 0, len(queries))

	for _, q := range queries {
		switch q[0] {
		case 1:
			obs = handleType1(q[1], obs, seg)
		case 2:
			results = append(results, handleType2(q[1], q[2], obs, seg))
		}
	}
  
	return results
}
