/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findBottomLeftValue(root *TreeNode) int {
    que := make([]*TreeNode, 0)
    que = append(que, root)
    res := root.Val

    for len(que) > 0 {
        n := len(que)
        for i := 0; i < n; i++ {
            node := que[0]
            que = que[1:]

            if (i == 0) {
                res = node.Val
            }

            if (node.Left != nil) {
                que = append(que, node.Left)
            }

            if (node.Right != nil) {
                que = append(que, node.Right)
            }
        }
    }

    return res
}