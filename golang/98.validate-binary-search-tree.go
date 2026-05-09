/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

import (
  "math"
)

func isValidBST(root *TreeNode) bool {

  var dfs func(*TreeNode, int, int) bool
  dfs = func(node *TreeNode, left, right int) bool {
    if node == nil {
      return true
    }

    if left < node.Val && node.Val < right {
      return dfs(node.Left, left, node.Val) && dfs(node.Right, node.Val, right)
    }

    return false
  }

  return dfs(root, math.MinInt, math.MaxInt)
}