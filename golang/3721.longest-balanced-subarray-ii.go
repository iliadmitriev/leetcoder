package main

// Segment Tree Structure
type SegmentTree struct {
	treeMin []int
	treeMax []int
	lazy    []int
	n       int
}

func NewSegmentTree(n int) *SegmentTree {
	size := 4 * n
	return &SegmentTree{
		treeMin: make([]int, size),
		treeMax: make([]int, size),
		lazy:    make([]int, size),
		n:       n,
	}
}

func (st *SegmentTree) Build(data []int, node, start, end int) {
	if start == end {
		st.treeMin[node] = data[start]
		st.treeMax[node] = data[start]
	} else {
		mid := (start + end) / 2
		st.Build(data, 2*node, start, mid)
		st.Build(data, 2*node+1, mid+1, end)
		st.treeMin[node] = min(st.treeMin[2*node], st.treeMin[2*node+1])
		st.treeMax[node] = max(st.treeMax[2*node], st.treeMax[2*node+1])
	}
}

func (st *SegmentTree) push(node int) {
	if st.lazy[node] != 0 {
		lz := st.lazy[node]

		st.treeMin[2*node] += lz
		st.treeMax[2*node] += lz
		st.lazy[2*node] += lz

		st.treeMin[2*node+1] += lz
		st.treeMax[2*node+1] += lz
		st.lazy[2*node+1] += lz

		st.lazy[node] = 0
	}
}

func (st *SegmentTree) Update(node, start, end, l, r, val int) {
	if l > end || r < start {
		return
	}

	if l <= start && end <= r {
		st.treeMin[node] += val
		st.treeMax[node] += val
		st.lazy[node] += val
		return
	}

	st.push(node)
	mid := (start + end) / 2
	st.Update(2*node, start, mid, l, r, val)
	st.Update(2*node+1, mid+1, end, l, r, val)

	st.treeMin[node] = min(st.treeMin[2*node], st.treeMin[2*node+1])
	st.treeMax[node] = max(st.treeMax[2*node], st.treeMax[2*node+1])
}

func (st *SegmentTree) FindLastZero(node, start, end, minIdx int) int {
	if end < minIdx {
		return -1
	}

	if st.treeMin[node] > 0 || st.treeMax[node] < 0 {
		return -1
	}

	if start == end {
		if st.treeMin[node] == 0 {
			return start
		}
		return -1
	}

	st.push(node)
	mid := (start + end) / 2

	res := st.FindLastZero(2*node+1, mid+1, end, minIdx)
	if res != -1 {
		return res
	}

	return st.FindLastZero(2*node, start, mid, minIdx)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func longestBalanced(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}

	allE := make(map[int]struct{})
	allO := make(map[int]struct{})
	for _, x := range nums {
		if x%2 != 0 {
			allO[x] = struct{}{}
		} else {
			allE[x] = struct{}{}
		}
	}

	if len(allE) == len(allO) {
		return n
	}
	if len(allE) == 0 || len(allO) == 0 {
		return 0
	}

	nextOcc := make([]int, n)
	for i := range nextOcc {
		nextOcc[i] = n
	}
	lastSeen := make(map[int]int)
	for i := n - 1; i >= 0; i-- {
		val := nums[i]
		if idx, ok := lastSeen[val]; ok {
			nextOcc[i] = idx
		}
		lastSeen[val] = i
	}

	initialBalance := make([]int, n)
	currE := make(map[int]struct{})
	currO := make(map[int]struct{})
	bal := 0

	for i, x := range nums {
		if x%2 != 0 {
			if _, exists := currO[x]; !exists {
				bal--
				currO[x] = struct{}{}
			}
		} else {
			if _, exists := currE[x]; !exists {
				bal++
				currE[x] = struct{}{}
			}
		}
		initialBalance[i] = bal
	}

	st := NewSegmentTree(n)
	st.Build(initialBalance, 1, 0, n-1)

	maxLen := 0
	for l := 0; l < n; l++ {
		idx := st.FindLastZero(1, 0, n-1, l)
		if idx != -1 {
			if idx-l+1 > maxLen {
				maxLen = idx - l + 1
			}
		}

		if l < n-1 {
			endRange := nextOcc[l] - 1
			if endRange >= l+1 {
				delta := 1
				if nums[l]%2 == 0 {
					delta = -1
				}
				st.Update(1, 0, n-1, l+1, endRange, delta)
			}
		}
	}

	return maxLen
}