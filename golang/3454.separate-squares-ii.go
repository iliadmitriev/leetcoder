// SegmentTree tracks the total length of the union of active intervals
// over the compressed 1D coordinate space.
// It supports adding/removing intervals and querying the total covered length
type SegmentTree struct {
	// count[pos] - number of active interval that fully cover the segment
	count []int

	// covered[pos] - actual length of union of active intervals within
	// the segment represented by the node 'pos'. This is what we ultimately query.
	covered []int

	// xs - ascending sorted list of all deduplicated endpoints (x-coordinates).
	xs []int

	// n - number of all elementary segments between itervals (len(xs) - 1).
	n int
}

func NewSegmentTree(xs []int) *SegmentTree {
	n := len(xs) - 1
	return &SegmentTree{
		count:   make([]int, 4*n),
		covered: make([]int, 4*n),
		xs:      xs,
		n:       n,
	}
}

// modify - updates segment tree by adding 'qval' (+1 for insert, -1 for remove)
// over the query interval [qleft, qright).
// Parameters:
//
//		qleft, qright: the real half-open [qleft, qright) iterval to update
//		qval: +1 to add an interval, -1 to remove one
//		left, right: indices in the 'elementary segment' array that this node covers
//		             i.e. this node represents the real interval [xs[left], xs[right + 1])
//		pos: index of the current node in the segment tree arrays, 0-base heap layout:
//	       left child = 2 * parent + 1
//	       right child = 2 * parent + 2
func (st *SegmentTree) modify(qleft, qright, qval, left, right, pos int) {
	// case 1: out of range
	if qleft >= st.xs[right+1] || st.xs[left] >= qright {
		return
	}

	// case 2: fully covered
	if qleft <= st.xs[left] && st.xs[right+1] <= qright {
		st.count[pos] += qval
	} else {
		mid := (left + right) / 2 // split range

		// left child covers elementary segments [left, mid]
		// interval [xs[left], xs[mid + 1])
		st.modify(qleft, qright, qval, left, mid, 2*pos+1)

		// right child covers elementary segments [mid + 1, right)
		st.modify(qleft, qright, qval, mid+1, right, 2*pos+2)
	}

	// recompute covered[pos] after update children or count
	if st.count[pos] > 0 {
		// this node is fully covered by at least one active interval
		// so its covered lenght is
		st.covered[pos] = st.xs[right+1] - st.xs[left]
	} else {
		// not fully covered with any interval
		if left == right {
			st.covered[pos] = 0
		} else {
			// interval of parent equal to inteval of its childrens
			st.covered[pos] = st.covered[2*pos+1] + st.covered[2*pos+2]
		}
	}
}

// Update updates coverage by adding (qval=+1) or removing (qval=-1) the interval [qleft, qright).
// The root node (pos=0) covers all elementary segments: [0, n-1]
// which corresponds to the real interval [xs[0], xs[n-1]).
func (st *SegmentTree) Update(qleft, qright, qval int) {
	if st.n > 0 {
		st.modify(qleft, qright, qval, 0, st.n-1, 0)
	}
}

func (st *SegmentTree) Query() int {
	return st.covered[0]
}

func separateSquares(squares [][]int) float64 {
	// Event represents a horizontal edge of a square.
	type Event struct {
		y, delta, xl, xr int
	}

	events := []Event{}
	xsSet := make(map[int]bool) // all unique x-coords for compression

	for _, sq := range squares {
		x, y, l := sq[0], sq[1], sq[2]
		xr := x + l

		events = append(events, Event{y, 1, x, xr})      // bottom edge
		events = append(events, Event{y + l, -1, x, xr}) // top edge

		xsSet[x] = true
		xsSet[xr] = true
	}

	// sort by y coord ascending
	sort.Slice(events, func(i, j int) bool {
		return events[i].y < events[j].y
	})

	xs := slices.Sorted(maps.Keys(xsSet)) // go v1.23

	segTree := NewSegmentTree(xs)

	var (
		psum      []float64               // prefix sum of the area
		widths    []int                   // width (union length) just after each element
		totalArea float64   = 0.0         // total area of all squares (without overlap)
		prevY     int       = events[0].y // y - coord of previos event
	)

	for _, event := range events {
		y, delta, xl, xr := event.y, event.delta, event.xl, event.xr

		currentWidth := segTree.Query()

		totalArea += float64(currentWidth) * float64(y-prevY)

		segTree.Update(xl, xr, delta) // apply interval

		psum = append(psum, totalArea)
		widths = append(widths, segTree.Query())

		prevY = y
	}

	target := math.Ceil(totalArea / 2) // target rounded up
	// binary search for the target in sorted prefix sum
	idx := sort.Search(len(psum), func(i int) bool {
		return psum[i] >= target
	})
	idx-- // use prev interval border

	areaBase := psum[idx]
	width := widths[idx]
	yBase := events[idx].y

	// y = yBase + (totalArea/2 - areaBase) / width
	//   = yBase + (totalArea - 2 * areaBase) / (2 * width)

	return float64(yBase) + (totalArea-2*areaBase)/(2*float64(width))
}