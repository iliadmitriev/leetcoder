import (
	"fmt"
	"math"
)

// TreeOpFn idempotent function, which:
// fn(x, fn(x, y)) = fn(x, y)
// fn(x, i) = x
// where i - identity value
type TreeOpFn[T any] func(T, T) T

type SegmentTree[T any] struct {
	size     int         // real size of tree (not nodes, only non empty leaves)
	identity T           // default value for tree: fn(value, identity) == value
	tree     []T         // tree storage slice
	fn       TreeOpFn[T] // two operand function
}

func NewSegmentTree[T any](arr []T, identity T, fn TreeOpFn[T]) *SegmentTree[T] {
	size := len(arr)
	tree := make([]T, 2*size)

	// build tree
	// set leaves
	for i, val := range arr {
		tree[size+i] = val
	}

	// upward build nodes, O(n)
	for i := size - 1; i >= 0; i-- {
		tree[i] = identity
		tree[i] = fn(tree[i<<1], tree[i<<1|1])
	}

	return &SegmentTree[T]{
		size:     size,
		identity: identity,
		tree:     tree,
		fn:       fn,
	}
}

// Update tree[i] = val, O(log n)
func (t *SegmentTree[T]) Update(idx int, val T) {
	idx += t.size     // shift index to leaves
	t.tree[idx] = val // set value to leaf node

	// propagate tree update upwards from leaf
	for idx >>= 1; idx >= 0; idx >>= 1 {
		t.tree[idx] = t.fn(
			t.tree[idx<<1],
			t.tree[idx<<1|1],
		)
	}
}

// Query [left, right), O(log n)
func (t *SegmentTree[T]) Query(left, right int) T {
	res := t.identity // set default value
	size := t.size

	// shift left and right pointers to leaves
	// move upward from leaves to root
	for left, right = left+size, right+size; left < right; left, right = left>>1, right>>1 {
		if left&1 == 1 {
			res = t.fn(res, t.tree[left])
			left++ // after
		}

		if right&1 == 1 {
			right-- // before
			res = t.fn(res, t.tree[right])
		}
	}

	return res
}


func maxTotalValue(nums []int, k int) int64 {
	n := len(nums)

	stMin := NewSegmentTree(nums, math.MaxInt, func(a, b int) int { return min(a, b) })
	stMax := NewSegmentTree(nums, math.MinInt, func(a, b int) int { return max(a, b) })

	h := make([][3]int, n)
	for i := range h {
		h[i] = [3]int{stMax.Query(i, n) - stMin.Query(i, n), i, n}
	}

  down := func(i int) {
    for {
      l, r, mx := i << 1, i << 1 | 1, i

      if l < n && h[l][0] > h[mx][0] {
        mx = l
      }
      if r < n && h[r][0] > h[mx][0] {
        mx = r
      }
      if mx == i {
        break
      }
      h[mx], h[i] = h[i], h[mx]
      i = mx
    }
  }

  down(0)

	res := 0

	for range k {
		val, l, r := h[0][0], h[0][1], h[0][2]

		res += val

    newVal := 0

		if r-1 > l {
			newVal = stMax.Query(l, r-1) - stMin.Query(l, r-1)
      h[0][2] = r - 1
		}

    h[0][0] = newVal
    down(0)
	}

	return int64(res)
}