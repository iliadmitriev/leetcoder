
func isSubPath(head *ListNode, root *TreeNode) bool {
	if root == nil {
		return false
	}

	return __dfsSubPath(head, root) ||
		isSubPath(head, root.Left) ||
		isSubPath(head, root.Right)
}

func __dfsSubPath(head *ListNode, root *TreeNode) bool {
	if head == nil {
		return true
	}

	if root == nil {
		return false
	}

	if root.Val == head.Val {
		return __dfsSubPath(head.Next, root.Left) ||
			__dfsSubPath(head.Next, root.Right)
	}

	return false
}
