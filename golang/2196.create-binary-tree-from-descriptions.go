/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func createBinaryTree(descriptions [][]int) *TreeNode {
	if len(descriptions) == 0 {
		return nil
	}

	var root *TreeNode
	tree := make(map[int]*TreeNode, len(descriptions))
	hasParent := make(map[int]bool, len(descriptions))

	for _, desc := range descriptions {
		hasParent[desc[1]] = true

		if _, ok := tree[desc[0]]; !ok {
			tree[desc[0]] = &TreeNode{Val: desc[0]}
		}

		if _, ok := tree[desc[1]]; !ok {
			tree[desc[1]] = &TreeNode{Val: desc[1]}
		}

		if desc[2] == 1 {
			tree[desc[0]].Left = tree[desc[1]]
		} else {
			tree[desc[0]].Right = tree[desc[1]]
		}
	}

	for _, desc := range descriptions {
		if _, ok := hasParent[desc[0]]; !ok {
			root = tree[desc[0]]
			return root
		}
	}

	return root
}
