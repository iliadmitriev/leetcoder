/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func pairSum(head *ListNode) int {
	res := 0
	mid, end := head, head
	stack := make([]int, 0)

	for end != nil && end.Next != nil {
		stack = append(stack, mid.Val)
		mid = mid.Next
		end = end.Next.Next
	}

	for len(stack) > 0 && mid != nil {
		v1, v2 := mid.Val, stack[len(stack)-1]

		res = max(res, v1+v2)

		mid = mid.Next
		stack = stack[:len(stack)-1]
	}

	return res
}