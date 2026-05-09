/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func nodesBetweenCriticalPoints(head *ListNode) []int {
	if head == nil || head.Next == nil {
		return []int{-1, -1}
	}

	minDist, maxDist := -1, -1
	prev, curr, next := head, head.Next, head.Next.Next

	firstIdx, prevIdx := -1, -1

	for i := 0; next != nil; i++ {
		if (prev.Val < curr.Val && curr.Val > next.Val) ||
			(prev.Val > curr.Val && curr.Val < next.Val) {

			if firstIdx == -1 {
				firstIdx = i
			} else {
				maxDist = i - firstIdx
				if minDist == -1 {
					minDist = maxDist
				}
				minDist = min(minDist, i-prevIdx)
			}

			prevIdx = i
		}

		prev, curr, next = curr, next, next.Next
	}

	return []int{minDist, maxDist}
}
