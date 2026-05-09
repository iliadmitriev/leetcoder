func findSecondMinimumValue(root *TreeNode) int {
	inf := -1
	first, second := inf, inf

	q := make([]*TreeNode, 0)
	q = append(q, root)

	for len(q) > 0 {
		node := q[0]
		q = q[1:]

		if node.Val < first || first == inf {
			second = first
			first = node.Val
		} else if (node.Val < second || second == inf) && node.Val != first {
			second = node.Val
		}

		if node.Left != nil {
			q = append(q, node.Left)
		}

		if node.Right != nil {
			q = append(q, node.Right)
		}
	}

	return second
}
