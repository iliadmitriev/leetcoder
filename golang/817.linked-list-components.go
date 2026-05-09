/**
 * Definition for singly-linked list.
 */
package main

// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func numComponents(head *ListNode, nums []int) int {
	if head == nil || len(nums) == 0 {
		return 0
	}

	res := len(nums)

	toVisit := make(map[int]bool, res)
	for _, num := range nums {
		toVisit[num] = true
	}

	prev, cur := head, head.Next
	for cur != nil {
		if toVisit[prev.Val] && toVisit[cur.Val] {
			res--
		}
		prev, cur = cur, cur.Next
	}

	return res
}
