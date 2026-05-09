/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}

	fast, slow := head, head
	var prev, tmp *ListNode
	for fast != nil && fast.Next != nil {
		tmp = slow
		slow = slow.Next
		fast = fast.Next.Next

		tmp.Next = prev
		prev = tmp
	}

	if fast != nil {
		slow = slow.Next
	}

	for prev != nil && prev.Val == slow.Val {
		prev = prev.Next
		slow = slow.Next
	}

	if slow == nil && prev == nil {
		return true
	}

	return false
}
