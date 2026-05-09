import (
	"slices"
	"sort"
)

func findItinerary(tickets [][]string) []string {
	const start = "JFK"
	n := len(tickets)
	adj := make(map[string][]string)
	res := make([]string, 0, n+1) // number of itiniaries is number of airports + 1
	st := newStack[string](n + 1)

	for _, tick := range tickets {
		from, to := tick[0], tick[1]
		adj[from] = append(adj[from], to)
	}

	for _, routes := range adj {
		sort.Strings(routes)
	}

	st.push(start)
	for !st.empty() {
		from := st.top()

		if next, ok := adj[from]; ok && len(next) > 0 {
			to := next[0]
			adj[from] = next[1:]
			st.push(to)
		} else {
			_ = st.pop()
			res = append(res, from)
		}
	}

	slices.Reverse(res)
	return res
}

type stack[T any] []T

func newStack[T any](cap int) *stack[T] { st := make(stack[T], 0, cap); return &st }
func (s *stack[T]) len() int            { return len(*s) }
func (s *stack[T]) empty() bool         { return len(*s) == 0 }
func (s *stack[T]) top() T              { n := len(*s); return (*s)[n-1] }
func (s *stack[T]) pop() T              { n := len(*s); x := (*s)[n-1]; *s = (*s)[:n-1]; return x }
func (s *stack[T]) push(x T)            { *s = append(*s, x) }