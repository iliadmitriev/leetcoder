/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func NewListNodeIter(node *ListNode) func() int {
	return func() int {
		if node != nil {
			x := node.Val
			node = node.Next
			return x
		}

		return -1
	}
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
	res := make([][]int, m)
	for i := range res {
		res[i] = make([]int, n)
	}

	nextGen := NewListNodeIter(head)

	top, bottom, left, right := 0, m-1, 0, n-1

	for top < bottom && left < right {
		for i := left; i < right; i++ {
			res[top][i] = nextGen()
		}

		for i := top; i < bottom; i++ {
			res[i][right] = nextGen()
		}

		for i := right; i > left; i-- {
			res[bottom][i] = nextGen()
		}

		for i := bottom; i > top; i-- {
			res[i][left] = nextGen()
		}

		top++
		bottom--
		left++
		right--
	}

	for i := top; i <= bottom; i++ {
		for j := left; j <= right; j++ {
			res[i][j] = nextGen()
		}
	}

	return res
}
