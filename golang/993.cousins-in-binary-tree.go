
func isCousins(root *TreeNode, x int, y int) bool {
	if root == nil {
		return false
	}

	q := make([][2]*TreeNode, 0)
	q = append(q, [2]*TreeNode{root, nil})
	parentX, parentY := (*TreeNode)(nil), (*TreeNode)(nil)

	for len(q) > 0 {
		parentX, parentY = nil, nil
		for size := len(q); size > 0; size-- {
			node, parent := q[0][0], q[0][1]
			q = q[1:]

			if node.Val == x {
				parentX = parent
			}

			if node.Val == y {
				parentY = parent
			}

			if parentX != nil && parentY != nil {
				return parentX != parentY
			}

			if node.Left != nil {
				q = append(q, [2]*TreeNode{node.Left, node})
			}

			if node.Right != nil {
				q = append(q, [2]*TreeNode{node.Right, node})
			}
		}
	}

	return false
}
