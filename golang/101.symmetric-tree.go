/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSymmetric(root *TreeNode) bool {
  if root == nil {
    return true
  }

  var dfs func(*TreeNode, *TreeNode) bool
  dfs = func(left, right *TreeNode) bool {
    if left == nil && right == nil {
      return true
    }

    if left == nil || right == nil || left.Val != right.Val {
      return false
    }

    return dfs(left.Right, right.Left) && dfs(left.Left, right.Right) 
  }
    
  return dfs(root.Left, root.Right)
}