/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func reverseOddLevels(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}

	q := make([]*TreeNode, 0)
	q = append(q, root)

	for level := 0; len(q) > 0; level++ {

		if level%2 == 1 {
			for i, j := 0, len(q)-1; i < j; i, j = i+1, j-1 {
				q[i].Val, q[j].Val = q[j].Val, q[i].Val
			}
		}

		for n := len(q); n > 0; n-- {
			node := q[0]
			q = q[1:]

			if node.Left != nil {
				q = append(q, node.Left)
			}

			if node.Right != nil {
				q = append(q, node.Right)
			}

		}
	}

	return root
}
