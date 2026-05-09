package main

func sumOfLeftLeaves(root *TreeNode) int {
	return sumLeftLeaves(root, false)
}

func sumLeftLeaves(root *TreeNode, isLeft bool) int {
	if root == nil {
		return 0
	}

	if isLeft && root.Left == nil && root.Right == nil {
		return root.Val
	}

	return sumLeftLeaves(root.Left, true) + sumLeftLeaves(root.Right, false)
}
