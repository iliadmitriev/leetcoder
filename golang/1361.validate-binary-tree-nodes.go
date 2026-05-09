func findRoot(n int, left, right []int) []int {
    inorder := make([]int, n)
    for _, i := range left {
        if i != -1 {
            inorder[i]++
        }
    }
    for _, i := range right {
        if i != -1 {
            inorder[i]++
        }
    }
    res := make([]int, 0, n)
    for i, c := range inorder {
        if c == 0 {
            res = append(res, i)
        }
    }
    return res
}
func validateBinaryTreeNodes(n int, leftChild []int, rightChild []int) bool {
    // find root node, and put it to the stack
    stack := findRoot(n, leftChild, rightChild)
    // root should be only one
    if len(stack) != 1 {
        return false
    }
    // dfs from root node
    // looking for cycles and check if all nodes reachable
    vis := make([]bool, n)
    cnt := 0
    for len(stack) > 0 {
        node := stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]
        cnt++

        if leftChild[node] != -1 {
            if vis[leftChild[node]] {
                return false
            }
            vis[leftChild[node]] = true
            stack = append(stack, leftChild[node])
        }

        if rightChild[node] != -1 {
            if vis[rightChild[node]] {
                return false
            }
            vis[rightChild[node]] = true
            stack = append(stack, rightChild[node])
        }
    }
    return cnt == n
}