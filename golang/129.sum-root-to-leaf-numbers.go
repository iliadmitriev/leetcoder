/**
 * Definition for a binary tree node.
 */
package main

import "errors"

var NoNode = errors.New("no node")

// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

type Item struct {
	node  *TreeNode
	total int
}

func (i *Item) IsLeaf() bool {
	return i.node.Left == nil && i.node.Right == nil
}

func (i *Item) Total() int {
	return i.total*10 + i.node.Val
}

func (i *Item) GetLeft() (*TreeNode, error) {
	if i.node.Left == nil {
		return nil, NoNode
	}

	return i.node.Left, nil
}

func (i *Item) GetRight() (*TreeNode, error) {
	if i.node.Right == nil {
		return nil, NoNode
	}

	return i.node.Right, nil
}

func sumNumbers(root *TreeNode) int {
	res := 0

	if root == nil {
		return 0
	}

	st := make([]Item, 0)
	st = append(st, Item{root, 0})

	for len(st) > 0 {
		i := st[len(st)-1]
		st = st[:len(st)-1]

		if i.IsLeaf() {
			res += i.Total()
		}

		if v, err := i.GetLeft(); err == nil {
			st = append(st, Item{v, i.Total()})
		}

		if v, err := i.GetRight(); err == nil {
			st = append(st, Item{v, i.Total()})
		}
	}

	return res
}
