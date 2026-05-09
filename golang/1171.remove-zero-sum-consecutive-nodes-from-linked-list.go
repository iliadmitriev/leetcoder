/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeZeroSumSublists(head *ListNode) *ListNode {
    dummy := &ListNode{0, head}

    mp := make(map[int]*ListNode)
    mp[0] = dummy

    total := 0
    curr := dummy
    for (curr != nil) {
        total += curr.Val
        mp[total] = curr
        curr = curr.Next
    }

    total = 0
    curr = dummy
    for (curr != nil) {
        total += curr.Val
        curr.Next = mp[total].Next
        curr = curr.Next
    }
    
    return dummy.Next
}