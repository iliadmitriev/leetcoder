
func postorder(root *Node) []int {
	res := make([]int, 0)

	__postorder(root, func(node *Node) {
		res = append(res, node.Val)
	})

	return res
}

type StackNode struct {
	Node    *Node
	Visited bool
}

func __postorder(root *Node, f func(*Node)) {
	if root == nil {
		return
	}

	stack := []StackNode{{root, false}}

	var node StackNode

	for len(stack) > 0 {
		node, stack = stack[len(stack)-1], stack[:len(stack)-1]

		if !node.Visited {
			node.Visited = true
			stack = append(stack, node)

			for i := len(node.Node.Children) - 1; i >= 0; i-- {
				stack = append(stack, StackNode{node.Node.Children[i], false})
			}

		} else {
			f(node.Node)
		}
	}

}
