
func maxLevelSum(root *TreeNode) int {
	if root == nil {
		return 0
	}

	q := make([]*TreeNode, 0, 1)
	q = append(q, root)

	maxLevel := 1
	level := 1
	maxSum := root.Val

	for len(q) > 0 {
		cur := 0
		newQ := make([]*TreeNode, 0, len(q)*2)

		for _, node := range q {
			cur += node.Val

			if node.Left != nil {
				newQ = append(newQ, node.Left)
			}

			if node.Right != nil {
				newQ = append(newQ, node.Right)
			}
		}

		q = newQ
		if maxSum < cur {
			maxLevel = level
			maxSum = cur
		}
		level++
	}

	return maxLevel
}
