func modifiedList(nums []int, head *ListNode) *ListNode {
	res := &ListNode{}

	toRemove := make(map[int]bool, len(nums))
	for _, num := range nums {
		toRemove[num] = true
	}

	ptr := res
	for head != nil {
		if _, ok := toRemove[head.Val]; !ok {
			ptr.Next = head
			ptr = ptr.Next
		}

		head = head.Next
	}

	ptr.Next = nil

	return res.Next
}
