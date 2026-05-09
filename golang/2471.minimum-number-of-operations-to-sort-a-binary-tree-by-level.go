import "sort"

func minimumOperations(root *TreeNode) int {
	if root == nil {
		return 0
	}

	q := []*TreeNode{root}
	swaps := 0

	for len(q) > 0 {

		level := make([]int, 0, len(q))

		for l := len(q); l > 0; l-- {
			node := q[0]
			q = q[1:]

			level = append(level, node.Val)

			if node.Left != nil {
				q = append(q, node.Left)
			}

			if node.Right != nil {
				q = append(q, node.Right)
			}
		}

		swaps += getSwaps(level)
	}

	return swaps
}

func getSwaps(original []int) int {
	swaps := 0

	target := make([]int, len(original))
	copy(target, original)
	sort.Ints(target)
	pos := make(map[int]int, len(original))
	for i, v := range original {
		pos[v] = i
	}

	for i := 0; i < len(original); i++ {
		if original[i] == target[i] {
			continue
		}

		j := pos[target[i]] // find where is target now
		// swap
		pos[original[j]] = i
		pos[original[i]] = j
		original[i], original[j] = original[j], original[i]
		swaps++

	}

	return swaps
}
