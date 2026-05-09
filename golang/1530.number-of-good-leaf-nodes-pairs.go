func countPairs(root *TreeNode, distance int) int {
	count := 0
	_ = countPairsDfs(root, 0, distance, &count)

	return count
}

func countPairsDfs(node *TreeNode, depth int, distance int, count *int) []int {
	if node == nil {
		return []int{}
	}

	if node.Left == nil && node.Right == nil {
		return []int{depth}
	}

	left := countPairsDfs(node.Left, depth+1, distance, count)
	right := countPairsDfs(node.Right, depth+1, distance, count)

	for _, l := range left {
		for _, r := range right {
			if l+r-2*depth <= distance {
				*count++
			}
		}
	}

	all := make([]int, 0, len(left)+len(right))
	for _, l := range left {
		if l-depth <= distance {
			all = append(all, l)
		}
	}

	for _, r := range right {
		if r-depth <= distance {
			all = append(all, r)
		}
	}

	return all
}
