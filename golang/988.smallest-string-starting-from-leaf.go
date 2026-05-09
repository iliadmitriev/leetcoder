/**
 * Definition for a binary tree node.
 */
// package main
//
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func smallestFromLeafUtil(node *TreeNode, st string) string {
	val := string(node.Val+'a') + st

	if node.Left == nil && node.Right == nil {
		return val
	}

	var right, left string

	if node.Right != nil {
		right = smallestFromLeafUtil(node.Right, val)
	}

	if node.Left != nil {
		left = smallestFromLeafUtil(node.Left, val)
	}

	if node.Left == nil {
		return right
	}

	if node.Right == nil {
		return left
	}

	if left < right {
		return left
	}

	return right
}

func smallestFromLeaf(root *TreeNode) string {
	return smallestFromLeafUtil(root, "")
}
