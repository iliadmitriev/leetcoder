/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	res := make([][]int, 0)
	q := []*TreeNode{root}
	sw := true

	for len(q) > 0 {
		sz := len(q)
		level := make([]int, sz)

		for i := 0; i < sz; i++ {
			node := q[i]
			if sw {
				level[i] = node.Val

			} else {
				level[sz-i-1] = node.Val
			}
      
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
		}

		q = q[sz:]
		res = append(res, level)
		sw = !sw
	}

	return res
}