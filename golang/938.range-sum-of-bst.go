/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rangeSumBST(root *TreeNode, low int, high int) int {
    if root == nil {
        return 0
    }

    st := []*TreeNode{ root }
    res := 0
    var node *TreeNode

    for len(st) > 0 {

        node = st[len(st) - 1]
        st = st[:len(st) - 1]

        if low <= node.Val && node.Val <= high {
            res += node.Val
        }

        if node.Right != nil && node.Val <= high {
            st = append(st, node.Right)
        }

        if node.Left != nil && low <= node.Val {
            st = append(st, node.Left)
        }
    }

    return res
}