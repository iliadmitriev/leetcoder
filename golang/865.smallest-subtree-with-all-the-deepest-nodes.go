
func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
	var dfs func(*TreeNode, int) (*TreeNode, int)

	dfs = func(node *TreeNode, depth int) (*TreeNode, int) {
		if node == nil {
			return nil, 0
		}

		left, leftDepth := dfs(node.Left, depth+1)
		right, rightDepth := dfs(node.Right, depth+1)

		switch {
		case left == nil && right == nil:
			return node, depth
		case leftDepth > rightDepth:
			return left, leftDepth
		case rightDepth > leftDepth:
			return right, rightDepth
		default:
			return node, leftDepth
		}
	}

	node, _ := dfs(root, 0)

	return node
}
