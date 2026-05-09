/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(node *TreeNode, cache int) int {
    if node == nil {
        return 0
    }

    cache ^= 1 << node.Val

    res := 0
    if node.Left == nil && node.Right == nil {
        if cache == 0 || cache & (cache - 1) == 0 {
            res += 1
        }
    }

    res += dfs(node.Left, cache)
    res += dfs(node.Right, cache)

    cache ^= 1 << node.Val

    return res
}

func pseudoPalindromicPaths (root *TreeNode) int {
    return dfs(root, 0)
}