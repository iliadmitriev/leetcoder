/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func replaceValueInTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}

	q := []*TreeNode{root}
	prevSum := root.Val

	for level := 0; len(q) > 0; level++ {
		levelSum := 0

		for size := len(q); size > 0; size-- {
			node := q[0]
			q = q[1:]

			node.Val = prevSum - node.Val

			brothers := 0
			if node.Left != nil {
				brothers += node.Left.Val
			}
			if node.Right != nil {
				brothers += node.Right.Val
			}

			if node.Left != nil {
				levelSum += node.Left.Val
				node.Left.Val = brothers
				q = append(q, node.Left)
			}

			if node.Right != nil {
				levelSum += node.Right.Val
				node.Right.Val = brothers
				q = append(q, node.Right)
			}
		}

		prevSum = levelSum
	}

	return root
}
