/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildGraph(root *TreeNode, gr map[int][]int) int {
    if root == nil {
        return 0
    }

    counter := 0
    st := [][2]*TreeNode{ [2]*TreeNode{ nil, root } }
    counter++
    var node, parent *TreeNode

    for len(st) > 0 {
        parent, node = st[len(st) - 1][0], st[len(st) - 1][1]
        st = st[:len(st) - 1]
        counter++

        if parent != nil {
            gr[parent.Val] = append(gr[parent.Val], node.Val)
            gr[node.Val] = append(gr[node.Val], parent.Val)
        }

        if node.Right != nil {
            st = append(st, [2]*TreeNode{node, node.Right})
        }

        if node.Left != nil {
            st = append(st, [2]*TreeNode{node, node.Left})
        }
    }

    return counter
}

func bfs(gr map[int][]int, start int, n int) int {
    level := -1

    q := make([]int, 0, n)
    vis := make(map[int]bool, n * 2)

    q = append(q, start)
    vis[start] = true

    var k int
    var node int

    for len(q) > 0 {
        k = len(q)
        for i := 0; i < k; i++ {
            node = q[0]
            q = q[1:]
            for _, child := range gr[node] {
                if vis[child] {
                    continue
                }

                q = append(q, child)
                vis[child] = true
            }
        }

        level++
    }

    return level
}

func amountOfTime(root *TreeNode, start int) int {
    gr := make(map[int][]int)
    n := buildGraph(root, gr)

    return bfs(gr, start, n)
}