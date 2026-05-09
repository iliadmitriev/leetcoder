type Node struct {
	Key        int
	Val        int
	Prev, Next *Node
}

type linkedList struct {
	count      int
	head, tail *Node
}

func newLinkedList() *linkedList {
	head, tail := &Node{Key: -1}, &Node{Key: -1}
	head.Next, tail.Prev = tail, head

	return &linkedList{
		count: 0,
		head:  head, // front
		tail:  tail, // back
	}
}

func (l *linkedList) PushFront(node *Node) {
	node.Prev, node.Next = l.head, l.head.Next

	l.head.Next, l.head.Next.Prev = node, node
	l.count++
}

func (l *linkedList) PushBack(node *Node) {
	node.Prev, node.Next = l.tail.Prev, l.tail

	l.tail.Prev, l.tail.Prev.Next = node, node
	l.count++
}

func (l *linkedList) PopFront() *Node {
	tmp := l.head.Next
	l.head.Next.Next.Prev, l.head.Next = l.head, l.head.Next.Next
  l.count--
	return tmp
}

func (l *linkedList) PopBack() *Node {
	tmp := l.tail.Prev
	l.tail.Prev.Prev.Next, l.tail.Prev = l.tail, l.tail.Prev.Prev
  l.count--
	return tmp
}

func (l *linkedList) Remove(node *Node) {
	node.Prev.Next, node.Next.Prev = node.Next, node.Prev
	node.Next, node.Prev = nil, nil
  l.count--
}

func (l *linkedList) PrintFront() {
	for tmp := l.head; tmp != nil; tmp = tmp.Next {
		fmt.Printf("[%d: %d]", tmp.Key, tmp.Val)
	}
	fmt.Println()
}

func (l *linkedList) PrintBack() {
	for tmp := l.tail; tmp != nil; tmp = tmp.Prev {
		fmt.Printf("[%d: %d]", tmp.Key, tmp.Val)
	}
	fmt.Println()
}

type LRUCache struct {
	cap   int
	list  *linkedList
	cache map[int]*Node
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		cap:   capacity,
		list:  newLinkedList(),
		cache: make(map[int]*Node),
	}
}

func (this *LRUCache) Get(key int) int {

	if node, ok := this.cache[key]; ok {
		this.list.Remove(node)
		this.list.PushFront(node)
		return node.Val
	}

	return -1
}

func (this *LRUCache) Put(key int, value int) {

	if node, ok := this.cache[key]; ok {
		node.Val = value
		this.list.Remove(node)
		this.list.PushFront(node)

		return
	}

	node := &Node{Key: key, Val: value}
	this.cache[key] = node
	this.list.PushFront(node)

	if this.list.count > this.cap {
		toRemove := this.list.PopBack()
		delete(this.cache, toRemove.Key)
	}
}

func (this *LRUCache) Print() {
	fmt.Println(this.cache)
	this.list.PrintFront()
	this.list.PrintBack()
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */