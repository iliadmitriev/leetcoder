/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import (
    "math"
)

type NodeIter struct{
    ptr *TreeNode
    done bool
}

func forEachInorder(root *TreeNode, fn func(*TreeNode)) {
    if root == nil {
        return
    }

    st := make([]NodeIter, 0)
    st = append(st, NodeIter{root, false})

    for len(st) > 0 {
        node := st[len(st) - 1]
        st = st[:len(st) - 1]

        // process done node
        if node.done {
            fn(node.ptr)
            continue
        }

        // add nodes reversed
        if node.ptr.Right != nil {
            st = append(st, NodeIter{node.ptr.Right, false})
        }
        st = append(st, NodeIter{node.ptr, true})
        if node.ptr.Left != nil {
            st = append(st, NodeIter{node.ptr.Left, false})
        }

    }

}

func findMode(root *TreeNode) []int {
    maxCounter := 0
    counter := 0
    prev := math.MinInt
    res := make([]int, 0)
    forEachInorder(root, func(node *TreeNode) {
        if node.Val == prev {
            counter++
        } else {
            counter = 1
        }

        if counter > maxCounter {
            res = res[:0]
            res = append(res, node.Val)
            maxCounter = counter
        } else if counter == maxCounter {
            res = append(res, node.Val)
        }
        prev = node.Val
    })
    return res
}