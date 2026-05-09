/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
  var d1, d2, carry, sum int
  s := &ListNode{}
  d := s

  for l1 != nil || l2 != nil || carry > 0 {
    if l1 != nil {
      d1 = l1.Val
      l1 = l1.Next
    } else {
      d1 = 0
    }

    if l2 != nil {
      d2 = l2.Val
      l2 = l2.Next
    } else {
      d2 = 0
    }

    sum = d1 + d2 + carry

    d.Next = &ListNode{Val: sum % 10}
    carry = sum / 10

    d = d.Next
  }

  return s.Next
}