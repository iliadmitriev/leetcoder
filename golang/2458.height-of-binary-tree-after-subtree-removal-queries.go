func treeQueries(root *TreeNode, queries []int) []int {
	heights := make(map[int]int)
	res := make([]int, len(queries))

	curMaxHeight := 0
	preOrder(root, heights, &curMaxHeight, 0, true)

	curMaxHeight = 0
	preOrder(root, heights, &curMaxHeight, 0, false)

	for i := range queries {
		res[i] = heights[queries[i]]
	}

	return res
}

func preOrder(node *TreeNode, height map[int]int, curMaxHeight *int, curHeight int, leftOrder bool) {
	if node == nil {
		return
	}

	if height[node.Val] < *curMaxHeight {
		height[node.Val] = *curMaxHeight
	}

	if *curMaxHeight < curHeight {
		*curMaxHeight = curHeight
	}

	if leftOrder {
		preOrder(node.Left, height, curMaxHeight, curHeight+1, true)
		preOrder(node.Right, height, curMaxHeight, curHeight+1, false)
	} else {
		preOrder(node.Right, height, curMaxHeight, curHeight+1, true)
		preOrder(node.Left, height, curMaxHeight, curHeight+1, false)
	}
}
