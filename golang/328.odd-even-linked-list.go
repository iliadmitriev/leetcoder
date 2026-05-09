/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func oddEvenList(head *ListNode) *ListNode {
    // if there is no head
    if head == nil {
        return head
    }

    // set odd head on 1st
    // set even head on 2nd
    odd_head, even_head := head, head.Next

    // start current odd and even pointers
    odd, even := odd_head, even_head

    // while there is one even and one next odd
    for ; even != nil && even.Next != nil; {
        // join odd to next odd (skip even)
        odd.Next = even.Next
        // move odd pointer forward
        odd = odd.Next

        // join even to next even (skip odd)
        even.Next = odd.Next
        // move even pointer forward
        even = even.Next
    }

    // finally, join odd tail to even head
    odd.Next = even_head
    // return odd head
    return odd_head  
}