/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func gen_subtree(start int, end int) []*TreeNode {
    if start > end {
        return []*TreeNode{nil}
    }

    var allTrees []*TreeNode
    for i := start; i <= end; i++ {
        leftTrees := gen_subtree(start, i - 1)
        rightTrees := gen_subtree(i + 1, end)

        for _, left := range leftTrees {
            for _, right := range rightTrees {
                current := &TreeNode{i, left, right}
                allTrees = append(allTrees, current)
            }
        }
    }
    return allTrees
}

func generateTrees(n int) []*TreeNode {
    if n == 0 {
        return []*TreeNode{}
    }
    return gen_subtree(1, n)
}