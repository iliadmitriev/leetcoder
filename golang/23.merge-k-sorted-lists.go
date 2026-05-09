/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

import (
	"container/heap"
)

type ListNodeMinHeap []*ListNode

func (h ListNodeMinHeap) Len() int           { return len(h) }
func (h ListNodeMinHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h ListNodeMinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *ListNodeMinHeap) Push(x any)        { *h = append(*h, x.(*ListNode)) }
func (h *ListNodeMinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func (h *ListNodeMinHeap) Empty() bool             { return len(*h) == 0 }
func (h *ListNodeMinHeap) TopItem() *ListNode      { return (*h)[0] }
func (h *ListNodeMinHeap) PopItem() *ListNode      { return heap.Pop(h).(*ListNode) }
func (h *ListNodeMinHeap) PushItem(item *ListNode) { heap.Push(h, item) }
func (h *ListNodeMinHeap) ReplaceTop(newItem *ListNode) *ListNode {
	if h.Len() == 0 {
		return nil
	}

	old := (*h)[0]
	(*h)[0] = newItem

	heap.Fix(h, 0)
	return old
}

func NewListNodeMinHeap(nodes []*ListNode) *ListNodeMinHeap {
	n := len(nodes)
	h := make(ListNodeMinHeap, 0, n)
	for _, node := range nodes {
		if node != nil {
			h = append(h, node)
		}
	}
	heap.Init(&h)
	return &h
}

func mergeKLists(lists []*ListNode) *ListNode {
	h := NewListNodeMinHeap(lists)
	res := &ListNode{}
	cur := res

	for !h.Empty() {
		top := h.TopItem()

		cur.Next = top
		cur = cur.Next
		top = top.Next

		if top != nil {
			_ = h.ReplaceTop(top)
		} else {
			_ = h.PopItem()
		}
	}

	return res.Next
}