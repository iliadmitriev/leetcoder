/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return root
	}

  if p.Val < root.Val && q.Val < root.Val { // both p & q is on the left
    return lowestCommonAncestor(root.Left, p, q)
  } else if root.Val < p.Val && root.Val < q.Val { // both p & q is on the right
    return lowestCommonAncestor(root.Right, p, q)
  }

  return root
}