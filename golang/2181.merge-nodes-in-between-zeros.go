/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeNodes(head *ListNode) *ListNode {
	cur, prev := head.Next, head

	for cur.Next != nil {
		if cur.Val == 0 {
			prev.Next = cur
			prev = cur
		}
		prev.Val += cur.Val
		cur = cur.Next
	}

	prev.Next = nil

	return head
}
