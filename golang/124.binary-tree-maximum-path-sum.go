/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxPathSum(root *TreeNode) int {

  pathMax := root.Val

  var dfs func(*TreeNode) int // returns subtree max and trunc max
  
  dfs = func(node *TreeNode) int {
    if node == nil {
      return 0
    }

    left := dfs(node.Left)
    right := dfs(node.Right)

    branch := node.Val + max(0, max(left, right))

    tree := node.Val + left + right

    pathMax = max(pathMax, max(branch, tree))

    return branch
  }

  dfs(root)
  return pathMax
}