/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func inorder(node *TreeNode, cb func(int)) {
    if node == nil {
        return
    }

    inorder(node.Left, cb)
    cb(node.Val)
    inorder(node.Right, cb)
}

func inorderTraversal(root *TreeNode) []int {
    out := make([]int, 0)

    inorder(root, func(i int) {
        out = append(out, i)
    })
    return out  
}