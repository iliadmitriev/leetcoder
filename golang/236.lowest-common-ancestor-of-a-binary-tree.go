/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func lowestCommonAncestor(node, p, q *TreeNode) *TreeNode {
  if node == nil || p == nil || q == nil {
    return nil
  }

  // cut path if only one the of the nodes is found
  // doesn't matter if the second node is not found yet:
  // there two options:
  // 1. can be found somewhere else
  // 2. it's on the same path with this current found node
  if node == p || node == q {
    return node
  }

  left := lowestCommonAncestor(node.Left, p, q)
  right := lowestCommonAncestor(node.Right, p, q)

  if left != nil && right != nil {
    return node
  }

  if left != nil {
    return left
  }

  if right != nil {
    return right
  }

  return nil
}
