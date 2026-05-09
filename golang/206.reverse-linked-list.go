/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// .             	p    c
//
// x <- 1 <- 2 <- 3    4
// n = c.n
// c.n = p
// p = c
// c = n
func reverseList(head *ListNode) *ListNode {
	p, c, n := (*ListNode)(nil), head, head

	for c != nil {
		n = c.Next
		c.Next = p
		p = c
		c = n
	}

	return p
}