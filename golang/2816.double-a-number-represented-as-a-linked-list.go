
func doubleIt(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	head = &ListNode{0, head}

	for cur, next := head, head.Next; next != nil; cur, next = next, next.Next {
		next.Val *= 2
		cur.Val += next.Val / 10
		next.Val %= 10
	}

	if head.Val == 0 {
		return head.Next
	}

	return head
}
