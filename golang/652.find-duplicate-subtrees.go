/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	cache := map[string]int{}

	res := []*TreeNode{}

	var dfs func(*TreeNode) string
	dfs = func(node *TreeNode) string {
		if node == nil {
			return "#"
		}


    left := dfs(node.Left)
    right := dfs(node.Right)

    key := fmt.Sprintf("%d(%s,%s)", node.Val, left, right)

    if cache[key] == 1 {
      res = append(res, node)
    }

    cache[key]++

    return key
	}


	dfs(root)
	return res
}