func pathSum(root *TreeNode, targetSum int) [][]int {
	res := [][]int{}
	path := []int{}
	pathSumDFS(root, &path, targetSum, &res)
	return res
}

func pathSumDFS(node *TreeNode, path *[]int, target int, res *[][]int) {
	if node == nil {
		return
	}

	target -= node.Val
	*path = append(*path, node.Val)

	if node.Left == nil && node.Right == nil && target == 0 {
		pathCopy := make([]int, len(*path))
		copy(pathCopy, *path)
		*res = append(*res, pathCopy)
	}

	pathSumDFS(node.Left, path, target, res)
	pathSumDFS(node.Right, path, target, res)

	*path = (*path)[:len(*path)-1]
}
