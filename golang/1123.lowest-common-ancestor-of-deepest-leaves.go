
func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	node, _ := lcaDeepestLeavesDFS(root, 0)
	return node
}

func lcaDeepestLeavesDFS(node *TreeNode, depth int) (*TreeNode, int) {
	if node == nil {
		return nil, 0
	}

	left, leftDepth := lcaDeepestLeavesDFS(node.Left, depth+1)
	right, rightDepth := lcaDeepestLeavesDFS(node.Right, depth+1)

	switch {
	case left == nil && right == nil:
		return node, depth
	case leftDepth > rightDepth:
		return left, leftDepth
	case leftDepth < rightDepth:
		return right, rightDepth
	}

	return node, leftDepth
}
