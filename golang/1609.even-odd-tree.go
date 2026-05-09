/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isEvenOddTree(root *TreeNode) bool {
    even := true
    que := make([]*TreeNode, 0)
    if root != nil{
        que = append(que, root)
    }

    for len(que) > 0 {
        n := len(que)
        pre := -1
        for i := 0; i < n; i++ {
            node := que[0]
            que = que[1:]

            if even {
                if node.Val % 2 == 0 { return false }
                if pre != -1 && !(pre < node.Val) { return false }
            } else {
                if node.Val % 2 == 1 { return false }
                if pre != -1 && !(pre > node.Val) { return false }
            }

            if node.Left != nil {
                que = append(que, node.Left)
            }

            if node.Right != nil {
                que = append(que, node.Right)
            }

            pre = node.Val
        }

        even = !even
    }

    return true
}