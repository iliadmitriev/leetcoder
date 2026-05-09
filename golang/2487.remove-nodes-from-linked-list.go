/**
 * Definition for singly-linked list.
 */
package main

// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func reverseLinkedList(head *ListNode) *ListNode {
	cur, prev := head, (*ListNode)(nil)
	for cur != nil {
		cur.Next, prev, cur = prev, cur, cur.Next
	}

	return prev
}

func removeNodes(head *ListNode) *ListNode {
	head = reverseLinkedList(head)

	cur := head
	for cur != nil {
		if cur.Next != nil && cur.Val > cur.Next.Val {
			cur.Next = cur.Next.Next
		} else {
			cur = cur.Next
		}
	}

	return reverseLinkedList(head)
}
