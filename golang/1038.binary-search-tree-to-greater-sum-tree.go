type Pack struct {
	Node *TreeNode
	Done bool
}

func revInorder(root *TreeNode, f func(*TreeNode)) {
	if root == nil {
		return
	}

	q := []Pack{{root, false}}
	var node *TreeNode
	var flag bool
	for len(q) > 0 {
		node = q[len(q)-1].Node
		flag = q[len(q)-1].Done
		q = q[:len(q)-1]

		if flag {
			f(node)
		} else {
			if node.Left != nil {
				q = append(q, Pack{node.Left, false})
			}
			q = append(q, Pack{node, true})
			if node.Right != nil {
				q = append(q, Pack{node.Right, false})
			}
		}
	}
}

func bstToGst(root *TreeNode) *TreeNode {
	total := 0

	revInorder(root, func(node *TreeNode) {
		total += node.Val
		node.Val = total
	})

	return root
}
