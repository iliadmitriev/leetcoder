/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode) {
	if head == nil || head.Next == nil {
		return
	}

	// find the middle of the list
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// split the list into two parts
	cur := slow.Next
	slow.Next = nil

	// reverse the second part
	var prev *ListNode
	for cur != nil {
		cur.Next, prev, cur = prev, cur, cur.Next
	}

	// merge the two parts
	a, b := head, prev
	var aa, bb *ListNode

	for a != nil && b != nil {
		aa, bb = a, b
		a, b = a.Next, b.Next
		aa.Next, bb.Next = bb, a
	}
}
