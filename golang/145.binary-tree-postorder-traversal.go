
func postorderTraversal(root *TreeNode) []int {
	res := make([]int, 0)
	postorderIterator(root, func(node *TreeNode) {
		res = append(res, node.Val)
	})

	return res
}

func postorderIterator(node *TreeNode, f func(*TreeNode)) {
	if node == nil {
		return
	}

	postorderIterator(node.Left, f)
	postorderIterator(node.Right, f)
	f(node)
}
