/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type State struct {
    node *TreeNode
    lo, hi int
}

func maxAncestorDiff(root *TreeNode) int {
    if root == nil {
        return 0
    }

    res := 0

    st := []State{ State{ root, root.Val, root.Val } }
    var top State
    var lo, hi int

    for len(st) > 0 {
        top = st[len(st) - 1]
        st = st[:len(st) - 1]

        if top.node == nil {
            res = max(res, top.hi - top.lo)
            continue
        }

        lo = min(top.lo, top.node.Val)
        hi = max(top.hi, top.node.Val)

        st = append(st, State{ top.node.Right, lo, hi })
        st = append(st, State{ top.node.Left, lo, hi })
    }

    return res
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
