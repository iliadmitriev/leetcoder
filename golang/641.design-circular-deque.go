type RingBuffer struct {
	Value      int
	Next, Prev *RingBuffer
}

type MyCircularDeque struct {
	capacity, size int
	front, tail    *RingBuffer
}

func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{
		capacity: k,
		size:     0,
		front:    nil,
		tail:     nil,
	}
}

func (this *MyCircularDeque) insertNode(value int) *RingBuffer {
	newNode := &RingBuffer{Value: value, Next: this.front, Prev: this.tail}
	if this.IsEmpty() {
		this.front, this.tail = newNode, newNode
	} else {
		this.front.Prev, this.tail.Next = newNode, newNode
	}

	return newNode
}

func (this *MyCircularDeque) InsertFront(value int) bool {
	if this.IsFull() {
		return false
	}

	this.front = this.insertNode(value)
	this.size++

	return true
}

func (this *MyCircularDeque) InsertLast(value int) bool {
	if this.IsFull() {
		return false
	}

	this.tail = this.insertNode(value)
	this.size++

	return true
}

func (this *MyCircularDeque) DeleteFront() bool {
	if this.IsEmpty() {
		return false
	}

	if this.front == this.tail {
		this.tail, this.front = nil, nil
	} else {
		this.front = this.front.Next
		this.front.Prev, this.tail.Next = this.tail, this.front
	}

	this.size--

	return true
}

func (this *MyCircularDeque) DeleteLast() bool {
	if this.IsEmpty() {
		return false
	}

	if this.front == this.tail {
		this.tail, this.front = nil, nil
	} else {
		this.tail = this.tail.Prev
		this.tail.Next, this.front.Prev = this.front, this.tail
	}

	this.size--

	return true
}

func (this *MyCircularDeque) GetFront() int {
	if this.IsEmpty() {
		return -1
	}

	return this.front.Value
}

func (this *MyCircularDeque) GetRear() int {
	if this.IsEmpty() {
		return -1
	}

	return this.tail.Value
}

func (this *MyCircularDeque) IsEmpty() bool {
	return this.size == 0
}

func (this *MyCircularDeque) IsFull() bool {
	return this.size == this.capacity
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */