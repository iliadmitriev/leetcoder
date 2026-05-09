/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, left int, right int) *ListNode {
    // set false start
    start := &ListNode{ Next: head }
    // reduce right by left
    right -= left

    // find left and prev pointers
    pre, cur := start, start.Next
    for ; left > 1; left-- {
        pre, cur = cur, cur.Next
    }

    // reverse
    var tail *ListNode
    for ; right > 0; right-- {
        tail = cur.Next // set tail node after current
        cur.Next = tail.Next // link current node to next node after tail
        tail.Next = pre.Next // link tail node to next to previous
        pre.Next = tail // link previous node to tail
    }
    return start.Next
}