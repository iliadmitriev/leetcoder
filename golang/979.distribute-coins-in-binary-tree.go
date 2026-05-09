func absV(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func distributeCoins(root *TreeNode) int {
	res := 0

	var dfs func(*TreeNode) (int, int)

	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}

		leftSize, leftCoins := dfs(node.Left)
		rightSize, rightCoins := dfs(node.Right)
		size := leftSize + rightSize + 1
		coins := leftCoins + rightCoins + node.Val

		res += absV(coins - size)

		return size, coins
	}

	_, _ = dfs(root)

	return res
}
