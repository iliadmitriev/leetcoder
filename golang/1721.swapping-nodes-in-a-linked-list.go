/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapNodes(head *ListNode, k int) *ListNode {
    dummy := &ListNode{-1, head}

    // find first node and it's predecessor
    prev, cur := dummy, dummy
    for ; k > 0; k-- {
        prev = cur
        cur = cur.Next
    }
    preFirst, first := prev, cur

    // find second node and it's predecessor
    preSecond, second := dummy, dummy
    for cur != nil {
        preSecond = second
        second = second.Next
        cur = cur.Next
    }

    // swap nodes
    preFirst.Next, preSecond.Next = preSecond.Next, preFirst.Next
    first.Next, second.Next = second.Next, first.Next

    return dummy.Next
}