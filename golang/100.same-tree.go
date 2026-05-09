/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func comp(a, b *TreeNode) bool {
	if a == nil && b == nil {
		return true
	}

	if a != nil && b != nil && a.Val == b.Val {
		return true
	}

	return false
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	que := make([][2]*TreeNode, 0)
	que = append(que, [2]*TreeNode{p, q})

	for len(que) > 0 {
		a, b := que[len(que)-1][0], que[len(que)-1][1]
		que = que[0 : len(que)-1]

		if !comp(a, b) {
			return false
		}

		if a != nil && b != nil {
			que = append(que, [2]*TreeNode{a.Right, b.Right})
			que = append(que, [2]*TreeNode{a.Left, b.Left})
		}
	}

	return true
}
