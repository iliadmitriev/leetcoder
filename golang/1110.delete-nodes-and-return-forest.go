func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	result := []*TreeNode{}
	toDel := map[int]bool{}

	for _, v := range to_delete {
		toDel[v] = true
	}

	delNodesDfs(root, !toDel[root.Val], toDel, &result)
	return result
}

func delNodesDfs(node *TreeNode, isRoot bool, toDel map[int]bool, result *[]*TreeNode) *TreeNode {
	if node == nil {
		return nil
	}

	if isRoot && !toDel[node.Val] {
		*result = append(*result, node)
	}

	node.Left = delNodesDfs(node.Left, toDel[node.Val], toDel, result)
	node.Right = delNodesDfs(node.Right, toDel[node.Val], toDel, result)

	if toDel[node.Val] {
		return nil
	}

	return node
}
