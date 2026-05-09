/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeLeaves struct {
    stack []*TreeNode
}

func NewTreeLeaves(root *TreeNode) *TreeLeaves {
    st := make([]*TreeNode, 0)
    if root != nil {
        st = append(st, root)
    }

    return &TreeLeaves{
        stack: st,
    }
}

func (t *TreeLeaves) Next() *TreeNode {
    var node *TreeNode

    for len(t.stack) > 0 {
    
        node = t.stack[len(t.stack) - 1]
        t.stack = t.stack[:len(t.stack) - 1]

        if node.Right != nil {
            t.stack = append(t.stack, node.Right)
        }

        if node.Left != nil {
            t.stack = append(t.stack, node.Left)
        }

        if node.Left == nil && node.Right == nil {
            return node
        }

    }

    return nil
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
    leaves1, leaves2 := NewTreeLeaves(root1), NewTreeLeaves(root2)
    var node1, node2 *TreeNode

    for {
        node1, node2 = leaves1.Next(), leaves2.Next()

        if node1 == nil && node2 == nil {
            return true
        }

        if node1 == nil || node2 == nil || node1.Val != node2.Val {
            return false
        }
    }

    return true
}