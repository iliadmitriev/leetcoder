/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// p.   c.   n    s
// d -> 1 -> 2 -> 3 -> 4 -> 5
// 
// swap:
// p.next = n
// c.next = s
// n.next = c
// move:
// p = c
// c = s
// n = c.next
func swapPairs(head *ListNode) *ListNode {
    d := &ListNode{-1, head}

    p, c, n, s := d, head, head, head
    for c != nil && c.Next != nil {
      // put next pointer
      n = c.Next
      s = n.Next

      // swap
      p.Next = n
      c.Next = s 
      n.Next = c

      p = c
      c = s
    } 

    return d.Next
}