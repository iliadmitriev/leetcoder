/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func binaryTreePaths(root *TreeNode) []string {
	res := make([]string, 0)
	path := make([]string, 0)
	binaryTreePathsDfs(root, &path, &res)
	return res
}

func binaryTreePathsDfs(node *TreeNode, path *[]string, res *[]string) {
	if node == nil {
		return
	}

	*path = append(*path, strconv.Itoa(node.Val))

	if node.Left == nil && node.Right == nil {
		*res = append(*res, strings.Join(*path, "->"))
		*path = (*path)[:len(*path)-1]
		return
	}

	binaryTreePathsDfs(node.Left, path, res)
	binaryTreePathsDfs(node.Right, path, res)
	*path = (*path)[:len(*path)-1]
}
