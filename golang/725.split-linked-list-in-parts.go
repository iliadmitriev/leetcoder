
func splitListToParts(head *ListNode, k int) []*ListNode {

	length := 0
	for ptr := head; ptr != nil; ptr = ptr.Next {
		length++
	}

	full := length / k
	partial := length % k

	parts := make([]*ListNode, k)

	prev := (*ListNode)(nil)

	for i := 0; i < k; i++ {
		// set start pointer
		parts[i] = head

		// calculate number of nodes
		chunkSize := full
		if partial > 0 {
			chunkSize++
			partial--
		}

		// iterate number of nodes in the chunk
		for ; chunkSize > 0; chunkSize-- {
			prev, head = head, head.Next
		}

		// cut
		if prev != nil {
			prev.Next = nil
		}
	}

	return parts
}
