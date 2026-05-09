/*

1  0  1  0  0
1  0  1  1  1
1  1  1  1  1
1  0  0  1  0

heights:

1  0  1  0  0
2  0  2  1  1
3  1  3  2  2
4  0  0  3  0

*/

func maximalRectangle(matrix [][]byte) int {
	n := len(matrix[0])
	maxRect := 0

	heights := make([]int, n+1)

	for _, row := range matrix {

		for j, x := range row {
			if x == '0' {
				heights[j] = 0 // reset
			} else {
				heights[j]++ // inc
			}
		}

		st := newStack(n + 1)
		for j, h := range heights {
			for !st.isEmpty() && heights[st.top()] > h {
				height := heights[st.pop()]
				width := j
				if !st.isEmpty() {
					width = j - st.top() - 1
				}
				maxRect = max(maxRect, width*height)
			}

			st.push(j)
		}

	}

	return maxRect
}

type stack []int

func newStack(cap int) *stack  { s := make(stack, 0, cap); return &s }
func (s *stack) len() int      { return len(*s) }
func (s *stack) isEmpty() bool { return len(*s) == 0 }
func (s *stack) top() int      { st := *s; return st[len(st)-1] }
func (s *stack) pop() int      { st := *s; x := st[len(st)-1]; *s = (*s)[:len(st)-1]; return x }
func (s *stack) push(x int)    { *s = append(*s, x) }