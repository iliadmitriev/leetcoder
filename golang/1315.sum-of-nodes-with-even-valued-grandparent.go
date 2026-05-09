/**
 * Definition for a binary tree node.
 */
func sumEvenGrandparent(root *TreeNode) int {
	if root == nil {
		return 0
	}

	q := make([][3]*TreeNode, 0)
	q = append(q, [3]*TreeNode{root, nil, nil})

	res := 0

	for len(q) > 0 {
		node, parent, grandParent := q[0][0], q[0][1], q[0][2]
		q = q[1:]

		if grandParent != nil && grandParent.Val%2 == 0 {
			res += node.Val
		}

		if node.Left != nil {
			q = append(q, [3]*TreeNode{node.Left, node, parent})
		}

		if node.Right != nil {
			q = append(q, [3]*TreeNode{node.Right, node, parent})
		}
	}

	return res
}
