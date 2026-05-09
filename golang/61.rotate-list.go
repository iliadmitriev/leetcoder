/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    last := head
    count := 0
    for ptr := head; ptr != nil; ptr = ptr.Next {
        count++
        last = ptr
    }

    // withdraw full rotations
    k %= count

    // no need to rotate
    if k == 0 {
        return head
    }

    // scroll down to rotation pos - 1
    new_start := head
    for j := 0; j < count - k - 1; j++ {
        new_start = new_start.Next
    }

    // connect tail with head
    last.Next = head
    // new start next after new start
    head = new_start.Next
    // cut new start
    new_start.Next = nil

    return head
}