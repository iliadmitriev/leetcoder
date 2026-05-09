/**
 * Definition for a Node.
 */

func maxDepth(root *Node) int {
	if root == nil {
		return 0
	}

	maxRes := 0
	for _, child := range root.Children {
		maxRes = max(maxRes, maxDepth(child))
	}

	return maxRes + 1
}
