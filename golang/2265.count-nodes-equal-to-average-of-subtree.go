/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type Rec struct{
    p *TreeNode
    ret bool
}

func averageOfSubtree(root *TreeNode) int {
    st := make([]Rec, 0)
    data := make([][2]int, 0) // list of tuples (total, count)

    st = append(st, Rec{root, false})
    res := 0

    for len(st) > 0 {
        node := st[len(st) - 1]
        st = st[:len(st) - 1]

        // if value returned: calclulate
        if node.ret {
            total := node.p.Val
            count := 1

            if node.p.Left != nil {
                total += data[len(data) - 1][0]
                count += data[len(data) - 1][1]
                data = data[:len(data) - 1]
            }

            if node.p.Right != nil {
                total += data[len(data) - 1][0]
                count += data[len(data) - 1][1]
                data = data[:len(data) - 1]
            }

            if total / count == node.p.Val {
                res++
            }

            data = append(data, [2]int{total, count})
            continue
        }
        // otherwise: postorder traversal
        node.ret = true
        st = append(st, node)

        if node.p.Right != nil {
            st = append(st, Rec{node.p.Right, false})
        }

        if node.p.Left != nil {
            st = append(st, Rec{node.p.Left, false})
        }
    }

    return res
}