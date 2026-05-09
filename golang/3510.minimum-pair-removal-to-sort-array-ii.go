import (
	"container/heap"
)

// Double linked list nodes
type Node struct {
	value int   // node value
	left  int   // left index
	prev  *Node // prev node in chain (nil for head)
	next  *Node // next node in chain (nil for tail)
}

// Min Proirity Queue
type Item struct {
	first  *Node // left node
	second *Node // right node
	cost   int   // pair sum (first priority)
	index  int   // pair index
}

type MinHeap []*Item

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
	h[i].index = i
	h[j].index = j
}
func (h MinHeap) Less(i, j int) bool {
	if h[i].cost == h[j].cost {
		return h[i].first.left < h[j].first.left
	}

	return h[i].cost < h[j].cost
}
func (h *MinHeap) Push(x any) {
	item := x.(*Item)
	item.index = h.Len()
	*h = append(*h, x.(*Item))
}
func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	item := old[n-1]
	item.index = -1
	*h = old[:n-1]
	return item
}

// domain
func (h *MinHeap) PushItem(x *Item) {
	heap.Push(h, x)
}
func (h *MinHeap) PopItem() *Item {
	return heap.Pop(h).(*Item)
}

/*

   [5, 2, 3, 1]
l: [5:0, 7:1, 5:2, 4:3]
h: [4:3, 5:2, 7:1]
*/

func minimumPairRemoval(nums []int) int {
	h := &MinHeap{}                        // minmal heap of nodes
	merged := make([]bool, len(nums))      // already merged indices
	dec := 0                               // number of out of decreasing nodes (nodes needed fixing)
	count := 0                             // count of merge operations performed
	head := &Node{value: nums[0], left: 0} // head node
	cur := head                            // pointer to current node

	for i := 1; i < len(nums); i++ {
		newNode := &Node{value: nums[i], left: i}
		cur.next = newNode
		newNode.prev = cur

		h.PushItem(&Item{
			first:  cur,
			second: newNode,
			cost:   cur.value + newNode.value,
		})

		if nums[i-1] > nums[i] {
			dec++
		}

		cur = newNode
	}

	for dec > 0 {
		item := h.PopItem()
		first := item.first
		second := item.second
		cost := item.cost

		// if left or right node in merged set or node sum outdated (left or right nodes have been replaced)
		if merged[first.left] || merged[second.left] || first.value+second.value != cost {
			continue
		}

    count++

		if first.value > second.value {
			dec--
		}

		// cut second node
		// p    f    s    n
		// * -> * -> * -> * ->
		prevNode := first.prev
		nextNode := second.next
		first.next = nextNode
		if nextNode != nil {
			nextNode.prev = first
		}

		if prevNode != nil {
			if prevNode.value > first.value && prevNode.value <= cost {
				dec--
			} else if prevNode.value <= first.value && prevNode.value > cost {
				dec++
			}
			h.PushItem(&Item{
				first:  prevNode,
				second: first,
				cost:   prevNode.value + cost,
			})
		}

		if nextNode != nil {
			if second.value > nextNode.value && cost <= nextNode.value {
				dec--
			} else if second.value <= nextNode.value && cost > nextNode.value {
				dec++
			}
			h.PushItem(&Item{
				first:  first,
				second: nextNode,
				cost:   cost + nextNode.value,
			})
		}

		first.value = cost
		merged[second.left] = true
	}

	return count
}