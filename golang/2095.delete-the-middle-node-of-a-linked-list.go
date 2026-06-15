/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
    if head == nil {
      return nil
    }

    res := &ListNode{Next: head}
    prev, mid, end := res, res.Next, res.Next
    
    for end != nil && end.Next != nil {
      prev = mid
      mid = mid.Next
      end = end.Next.Next
    }

    prev.Next = mid.Next

    return res.Next
}