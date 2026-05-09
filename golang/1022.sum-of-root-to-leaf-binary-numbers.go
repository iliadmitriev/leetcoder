/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumRootToLeaf(root *TreeNode) int {
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, val int) int {
		if node == nil {
			return 0
		}

		cur := (val << 1) + node.Val

		if node.Left == nil && node.Right == nil {
			return cur
		}

		return dfs(node.Left, cur) + dfs(node.Right, cur)
	}

	return dfs(root, 0)
}