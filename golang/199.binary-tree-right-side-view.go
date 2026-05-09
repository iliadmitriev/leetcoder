/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	q := []*TreeNode{root}
	res := []int{}

	for len(q) > 0 {
		prev := q[0]
		for range len(q) {
			node := q[0]
			q = q[1:]

			if node.Left != nil {
				q = append(q, node.Left)
			}

			if node.Right != nil {
				q = append(q, node.Right)
			}

			prev = node
		}

		res = append(res, prev.Val)
	}

	return res
}