import (
	"container/list"
	"fmt"
)

type AllOne struct {
	dataMap          map[string]*list.Element
	dataList         *list.List
	minHead, maxTail *list.Element
}

type AllOneNode struct {
	Freq int
	Keys map[string]bool
}

func NewAllOneNode(freq int) *AllOneNode {
	return &AllOneNode{Freq: freq, Keys: map[string]bool{}}
}

func (a *AllOneNode) GetAnyKey() string {
	for k, _ := range a.Keys {
		return k
	}

	return ""
}

func (a *AllOneNode) AddKey(key string) {
	a.Keys[key] = true
}

func (a *AllOneNode) DelKey(key string) {
	delete(a.Keys, key)
}

func (a *AllOneNode) IsEmpty() bool {
	return len(a.Keys) == 0
}

func Constructor() AllOne {
	lst := list.New()
	return AllOne{
		dataMap:  map[string]*list.Element{},
		dataList: lst,
		minHead:  lst.PushFront(NewAllOneNode(-1)),
		maxTail:  lst.PushBack(NewAllOneNode(-1)),
	}
}

func (this *AllOne) Inc(key string) {
	// if input key string is on the map
	if node, ok := this.dataMap[key]; ok {
		freq := node.Value.(*AllOneNode).Freq
		node.Value.(*AllOneNode).DelKey(key)
		nextNode := node.Next()
		nextFreq := nextNode.Value.(*AllOneNode).Freq

		if nextNode == this.maxTail || nextFreq != freq+1 {
			newNode := NewAllOneNode(freq + 1)
			newNode.AddKey(key)
			this.dataMap[key] = this.dataList.InsertBefore(newNode, nextNode)
		} else {
			nextNode.Value.(*AllOneNode).AddKey(key)
			this.dataMap[key] = nextNode
		}

		if node.Value.(*AllOneNode).IsEmpty() {
			this.dataList.Remove(node)
		}
		// if input key string is not on the map
	} else {
		firstNode := this.minHead.Next()

		if firstNode == this.maxTail || firstNode.Value.(*AllOneNode).Freq > 1 {
			newNode := NewAllOneNode(1)
			newNode.AddKey(key)
			this.dataMap[key] = this.dataList.InsertBefore(newNode, firstNode)
		} else {
			firstNode.Value.(*AllOneNode).AddKey(key)
			this.dataMap[key] = firstNode
		}
	}
}

func (this *AllOne) Dec(key string) {
	if _, ok := this.dataMap[key]; !ok {
		return
	}

	node := this.dataMap[key]
	node.Value.(*AllOneNode).DelKey(key)
	freq := node.Value.(*AllOneNode).Freq

	if freq == 1 {
		delete(this.dataMap, key)
	} else {
		prevNode := node.Prev()
		prevFreq := prevNode.Value.(*AllOneNode).Freq

		if prevNode == this.minHead || prevFreq != freq-1 {
			newNode := NewAllOneNode(freq - 1)
			newNode.AddKey(key)
			this.dataMap[key] = this.dataList.InsertAfter(newNode, prevNode)
		} else {
			prevNode.Value.(*AllOneNode).DelKey(key)
			this.dataMap[key] = prevNode
		}
	}

	if node.Value.(*AllOneNode).IsEmpty() {
		this.dataList.Remove(node)
	}
}

func (this *AllOne) GetMaxKey() string {
	maxNode := this.maxTail.Prev()
	if maxNode == this.minHead {
		return ""
	}

	return maxNode.Value.(*AllOneNode).GetAnyKey()
}

func (this *AllOne) GetMinKey() string {
	minNode := this.minHead.Next()
	if minNode == this.maxTail {
		return ""
	}

	return minNode.Value.(*AllOneNode).GetAnyKey()
}

func (this *AllOne) Print() {
	for k, v := range this.dataMap {
		fmt.Printf("%s: %d, ", k, v.Value.(*AllOneNode).Freq)
	}
	fmt.Println()
	for node := this.dataList.Front(); node != nil; node = node.Next() {
		fmt.Printf("{%d: %v} ", node.Value.(*AllOneNode).Freq, node.Value.(*AllOneNode).Keys)
	}
	fmt.Printf("\n-------\n")
}

/**
 * Your AllOne object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Inc(key);
 * obj.Dec(key);
 * param_3 := obj.GetMaxKey();
 * param_4 := obj.GetMinKey();
 */