func inorder(node *TreeNode, cb func(*TreeNode)) {
	if node == nil {
		return
	}
	inorder(node.Left, cb)
	cb(node)
	inorder(node.Right, cb)
}

func build(nodes []*TreeNode, left, right int) *TreeNode {
	if left > right {
		return nil
	}
	mid := (left + right) / 2
	node := nodes[mid]

	node.Left = build(nodes, left, mid-1)
	node.Right = build(nodes, mid+1, right)
	return node
}

func balanceBST(root *TreeNode) *TreeNode {
	buff := make([]*TreeNode, 0, 100)
	inorder(root, func(node *TreeNode) {
		buff = append(buff, node)
	})

	return build(buff, 0, len(buff)-1)
}
