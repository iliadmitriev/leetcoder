
func kthLargestLevelSum(root *TreeNode, k int) int64 {
	if root == nil {
		return -1
	}

	levels := make([]int, 0)

	q := []*TreeNode{root}

	for len(q) > 0 {
		levelSum := 0

		for levelSize := len(q); levelSize > 0; levelSize-- {
			node := q[0]
			q = q[1:]

			levelSum += node.Val
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}

		levels = append(levels, levelSum)
	}

	sort.Ints(levels)
	if k > len(levels) {
		return -1
	}

	return int64(levels[len(levels)-k])
}
