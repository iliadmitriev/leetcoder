func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	cur, mid := head, (*ListNode)(nil)

	for cur != nil && cur.Next != nil {
		g := gcdListNode(cur.Val, cur.Next.Val)
		mid = &ListNode{g, mid}
		cur.Next, mid.Next, cur = mid, cur.Next, cur.Next
	}

	return head
}

func gcdListNode(a, b int) int {
	if a < b {
		a, b = b, a
	}

	for b > 0 {
		a, b = b, a%b
	}

	return a
}
