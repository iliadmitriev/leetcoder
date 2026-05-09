/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
  var dfs func(*TreeNode) int
  dfs = func(node *TreeNode) int {
    if node == nil {
      return 0
    }

    return 1 + max(dfs(node.Left), dfs(node.Right))
  } 

  return dfs(root)
}