
type Queue []*TreeNode

func (q *Queue) Push(v *TreeNode) { *q = append(*q, v) }
func (q *Queue) Pop() *TreeNode   { v := (*q)[0]; *q = (*q)[1:]; return v }
func (q *Queue) Len() int         { return len(*q) }
func (q *Queue) Peek() *TreeNode  { return (*q)[0] }
func (q *Queue) Empty() bool      { return q.Len() == 0 }

func largestValues(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	levelMax := make([]int, 0)
	var q Queue
	q.Push(root)

	for !q.Empty() {
		curMax := q.Peek().Val

		for sz := q.Len(); sz > 0; sz-- {
			node := q.Pop()

			if node.Val > curMax {
				curMax = node.Val
			}

			if node.Left != nil {
				q.Push(node.Left)
			}

			if node.Right != nil {
				q.Push(node.Right)
			}
		}

		levelMax = append(levelMax, curMax)
	}

	return levelMax
}
