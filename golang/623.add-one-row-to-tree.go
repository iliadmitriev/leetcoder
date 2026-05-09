/**
 * Definition for a binary tree node.
 */
package main

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func dfs(node *TreeNode, val, depth, curDepth int) *TreeNode {
	if node == nil {
		return nil
	}

	if depth-1 == curDepth {
		node.Left = &TreeNode{Val: val, Left: node.Left, Right: nil}
		node.Right = &TreeNode{Val: val, Left: nil, Right: node.Right}
	} else if depth > curDepth {
		node.Left = dfs(node.Left, val, depth, curDepth+1)
		node.Right = dfs(node.Right, val, depth, curDepth+1)
	}

	return node
}

func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
	if depth == 1 {
		return &TreeNode{Val: val, Left: root}
	}

	return dfs(root, val, depth, 1)
}
