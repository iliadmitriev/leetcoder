func largestRectangleArea(heights []int) int {
    heights = append(heights, 0)

    n := len(heights)
    maxArea := 0

    st := newStack[int](n)

    for i, h := range heights {
        for !st.empty() && heights[st.top()] > h {
            height := heights[st.pop()]

            width := i
            if !st.empty() {
                // i - next smaller element (h < heights[st.top()])
                // st.top() - previous smaller element 
                width = i - st.top() - 1
            }

            maxArea = max(maxArea, width * height)
        }

        st.push(i)
    }

    return maxArea
}

type stack[T any] []T

func newStack[T any](cap int) *stack[T] { st:=make(stack[T], 0, cap); return &st }
func (s *stack[T]) len() int { return len(*s) }
func (s *stack[T]) empty() bool { return len(*s) == 0 }
func (s *stack[T]) top() T { return (*s)[len(*s) - 1] }
func (s *stack[T]) pop() T { x := (*s)[len(*s) - 1]; *s = (*s)[:len(*s) - 1]; return x }
func (s *stack[T]) push(x T) { *s = append(*s, x) }