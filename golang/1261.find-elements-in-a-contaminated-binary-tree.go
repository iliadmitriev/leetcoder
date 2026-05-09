type FindElements struct {
	nodes map[int]bool
}

func Constructor(root *TreeNode) FindElements {
	fe := FindElements{}
	fe.nodes = make(map[int]bool)
	fe.recover(root, 0)

	return fe
}

func (this *FindElements) recover(node *TreeNode, val int) {
	if node == nil {
		return
	}

	this.nodes[val] = true

	this.recover(node.Left, val*2+1)
	this.recover(node.Right, val*2+2)
}

func (this *FindElements) Find(target int) bool {
	return this.nodes[target]
}
