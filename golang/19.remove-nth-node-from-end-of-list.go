/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
  end := head
  for ; n > 0; n-- {
    end = end.Next
  }

  prev, cur := (*ListNode)(nil), head

  for end != nil {
    prev = cur
    cur = cur.Next
    end = end.Next
  }

  if prev == nil {
    return head.Next
  }

  prev.Next = cur.Next
  return head
}