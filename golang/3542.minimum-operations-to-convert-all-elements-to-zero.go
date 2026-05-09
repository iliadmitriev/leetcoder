
type stack []int

func NewStack(n int) *stack {
	st := make(stack, 0, n)
	return &st
}

func (s *stack) push(v int) { *s = append(*s, v) }
func (s *stack) pop() int   { v := (*s)[len(*s)-1]; *s = (*s)[:len(*s)-1]; return v }
func (s *stack) top() int   { return (*s)[len(*s)-1] }

func minOperations(nums []int) int {
	n := len(nums)
	st := NewStack(n)
	st.push(0)

	ops := 0

	for _, num := range nums {

		for st.top() > num {
			st.pop()
		}

		if st.top() == num {
			continue
		}

		ops++
		st.push(num)
	}

	return ops
}
