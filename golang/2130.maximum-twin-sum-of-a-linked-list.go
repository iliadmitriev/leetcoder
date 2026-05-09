/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func findMid(head *ListNode) *ListNode {
    fast, slow := head, head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }
    return slow
}

func revFromNode(head *ListNode) *ListNode {
    var pre, cur, nxt *ListNode = nil, head, nil

    for cur != nil {
        nxt = cur.Next
        cur.Next = pre

        pre = cur
        cur = nxt
    }

    return pre
}

func max(a,b int) int {
    if a > b {
        return a
    }
    return b
}

func pairSum(head *ListNode) int {
    mid := findMid(head)
    second := revFromNode(mid)

    res := 0
    for head != nil && second != nil {
        res = max(res, head.Val + second.Val)
        head = head.Next
        second = second.Next
    }
    return res
}