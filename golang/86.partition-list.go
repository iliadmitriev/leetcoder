/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {
    less, other := &ListNode{}, &ListNode{}
    less_head, other_head := less, other

    for head != nil {
        if head.Val < x {
            less.Next = head
            less = less.Next
        } else {
            other.Next = head
            other = other.Next
        }
        head = head.Next
    }

    less.Next = other_head.Next
    other.Next = nil

    return less_head.Next
}