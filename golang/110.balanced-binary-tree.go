/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {

	var dfs func(*TreeNode) (bool, int)
	dfs = func(node *TreeNode) (bool, int) {
		if node == nil {
			return true, 0
		}

		left, heightLeft := dfs(node.Left)
		right, heightRight := dfs(node.Right)

		heightLeft, heightRight = max(heightLeft, heightRight), min(heightLeft, heightRight)

		return left && right && (heightLeft-heightRight <= 1), heightLeft + 1
	}

	res, _ := dfs(root)
	return res
}