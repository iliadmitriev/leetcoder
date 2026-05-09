/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type StackNode struct {
    node *TreeNode
    pr bool
}

func diameterOfBinaryTree(root *TreeNode) int {
    stack := make([]StackNode, 0)
    stack = append(stack, StackNode{root, false})

    res := 0

    ret := map[*TreeNode]int{nil: -1}

    for len(stack) > 0 {
        node := stack[len(stack) - 1]
        stack = stack[0: len(stack) - 1]

        if node.pr {
            left := ret[node.node.Left]
            right := ret[node.node.Right]
            res = max(res, left + right + 2)
            ret[node.node] = max(left, right) + 1

        } else {
            node.pr = true
            stack = append(stack, node)

            if node.node.Right != nil {
                stack = append(stack, StackNode{ node.node.Right, false })
            }

            if node.node.Left != nil {
                stack = append(stack, StackNode{ node.node.Left, false })
            }
        }
    }

    return res
}