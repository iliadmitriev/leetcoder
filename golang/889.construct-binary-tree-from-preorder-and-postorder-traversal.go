
type nodeStack []*TreeNode

func (s *nodeStack) push(node *TreeNode) {
	(*s) = append(*s, node)
}

func (s *nodeStack) pop() *TreeNode {
	x := (*s)[len(*s)-1]
	(*s) = (*s)[:len(*s)-1]
	return x
}

func (s *nodeStack) top() *TreeNode {
	return (*s)[len(*s)-1]
}

func (s *nodeStack) empty() bool {
	return len(*s) == 0
}

func newNodeStack(n int) *nodeStack {
	st := make(nodeStack, 0, n)
	return &st
}

func constructFromPrePost(preorder []int, postorder []int) *TreeNode {
	N := len(preorder)
	st := newNodeStack(N)
	node := (*TreeNode)(nil)
	i, j := 0, 0

	for j < N {
		if !st.empty() && st.top().Val == postorder[j] {
			node = st.pop()
			j++
			continue
		}

		node = &TreeNode{Val: preorder[i]}
		i++

		if !st.empty() {
			if st.top().Left == nil {
				st.top().Left = node
			} else {
				st.top().Right = node
			}
		}

		st.push(node)

	}

	return node
}
