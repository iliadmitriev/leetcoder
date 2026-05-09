
func helper(preorder []int, bound int, pos *int) *TreeNode {
	if *pos >= len(preorder) || preorder[*pos] > bound {
		return nil
	}

	val := preorder[*pos]
	node := &TreeNode{Val: val}
	*pos++

	node.Left = helper(preorder, val, pos)
	node.Right = helper(preorder, bound, pos)

	return node
}

func bstFromPreorder(preorder []int) *TreeNode {
	pos := 0
	return helper(preorder, math.MaxInt, &pos)
}
