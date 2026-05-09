
type RangeTree struct {
	start, end  int
	left, right *RangeTree
}

func (t *RangeTree) insert(start, end int) bool {
	if end <= t.start {

		if t.left != nil {
			return t.left.insert(start, end)
		}

		t.left = &RangeTree{start: start, end: end}
		return true

	} else if t.end <= start {

		if t.right != nil {
			return t.right.insert(start, end)
		}

		t.right = &RangeTree{start: start, end: end}
		return true
	}

	return false
}

type MyCalendar struct {
	root *RangeTree
}

func Constructor() MyCalendar {
	return MyCalendar{}
}

func (this *MyCalendar) Book(start int, end int) bool {
	if this.root != nil {
		return this.root.insert(start, end)
	}

	this.root = &RangeTree{start: start, end: end}
	return true
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */