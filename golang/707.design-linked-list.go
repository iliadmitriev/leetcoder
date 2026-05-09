package main

type DLNode struct {
	val        int
	next, prev *DLNode
}

type MyLinkedList struct {
	head, tail *DLNode
	size       int
}

func Constructor() MyLinkedList {
	return MyLinkedList{}
}

func (this *MyLinkedList) getNode(index int) *DLNode {
	if index < 0 || index >= this.size {
		return nil
	}

	cur := (*DLNode)(nil)
	fromHead := index <= this.size/2

	if fromHead {
		cur = this.head
	} else {
		cur = this.tail
		index = this.size - index - 1
	}

	for index > 0 && cur != nil {
		if fromHead {
			cur = cur.next
		} else {
			cur = cur.prev
		}
		index--
	}

	return cur
}

func (this *MyLinkedList) addNodeBetween(node, prev, next *DLNode) {
	node.next = next
	node.prev = prev

	if prev != nil {
		prev.next = node
	} else {
		this.head = node
	}

	if next != nil {
		next.prev = node
	} else {
		this.tail = node
	}

	this.size++
}

func (this *MyLinkedList) removeNode(node *DLNode) {
	prev, next := node.prev, node.next

	if prev != nil {
		prev.next = next
	} else {
		this.head = next
	}

	if next != nil {
		next.prev = prev
	} else {
		this.tail = prev
	}

	this.size--
}

func (this *MyLinkedList) Get(index int) int {
	if index < 0 || index >= this.size {
		return -1
	}

	pos := this.getNode(index)
	if pos == nil {
		return -1
	}

	return pos.val
}

func (this *MyLinkedList) AddAtHead(val int) {
	this.addNodeBetween(&DLNode{val: val}, nil, this.head)
}

func (this *MyLinkedList) AddAtTail(val int) {
	this.addNodeBetween(&DLNode{val: val}, this.tail, nil)
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 || index > this.size {
		return
	}

	if index == 0 {
		this.AddAtHead(val)
		return
	}

	if index == this.size {
		this.AddAtTail(val)
		return
	}

	pos := this.getNode(index)
	if pos == nil {
		return
	}

	this.addNodeBetween(&DLNode{val: val}, pos.prev, pos)
}

func (this *MyLinkedList) DeleteAtIndex(index int) {
	pos := this.getNode(index)

	if pos == nil {
		return
	}

	this.removeNode(pos)
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */