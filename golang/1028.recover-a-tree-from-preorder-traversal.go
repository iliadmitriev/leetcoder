type stackNodes []*TreeNode

func (s *stackNodes) push(node *TreeNode) {
	*s = append(*s, node)
}

func (s *stackNodes) pop() *TreeNode {
	node := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return node
}

func (s *stackNodes) empty() bool {
	return len(*s) == 0
}

func (s *stackNodes) top() *TreeNode {
	return (*s)[len(*s)-1]
}

func (s *stackNodes) size() int {
	return len(*s)
}

func (s *stackNodes) bottom() *TreeNode {
	if s.empty() {
		return nil
	}

	return (*s)[0]
}

func recoverFromPreorder(traversal string) *TreeNode {
	N := len(traversal)
	i := 0
	st := &stackNodes{}

	for i < N {
		level, value := 0, 0
		for i < N && traversal[i] == '-' {
			level++
			i++
		}

		for i < N && traversal[i] != '-' {
			value = value*10 + int(traversal[i]-'0')
			i++
		}

		for st.size() > level {
			st.pop()
		}

		node := &TreeNode{Val: value}
		if !st.empty() {
			if st.top().Left == nil {
				st.top().Left = node
			} else {
				st.top().Right = node
			}
		}

		st.push(node)
	}

	return st.bottom()
}
