/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (this NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (this NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (this *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (this NestedInteger) GetList() []*NestedInteger {}
 */

type NestedIterator struct {
	pull func() (int, bool)

	// prefetch cache first value
	next    int
	hasNext bool
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
	pull, _ := iter.Pull(nested(nestedList))

	next, hasNext := pull()

	return &NestedIterator{
		pull:    pull,
		next:    next,
		hasNext: hasNext,
	}

}

func (this *NestedIterator) Next() int {
	ret := this.next

	this.next, this.hasNext = this.pull()

	return ret
}

func (this *NestedIterator) HasNext() bool {
	return this.hasNext
}

func nested(nestedList []*NestedInteger) iter.Seq[int] {
  return func(yield func(int) bool) {
    for _, item := range nestedList {
      // if item is a scalar, then return it
      if item.IsInteger() {
        if !yield(item.GetInteger()) {
          return
        }

        continue
      }
      // otherwise it's a list
      for v := range nested(item.GetList()) {
        if !yield(v) {
          return
        }
      }
    }
  }
}