func processStr(s string) string {
	res := newBuffer(len(s))

	for i := range len(s) {
		ch := s[i]

		switch ch {
		case '*':
			res.pop()
		case '#':
			res.dup()
		case '%':
			res.rev()
		default:
      res.push(ch)
		}
	}

	return res.out()
}

type buffer []byte

func newBuffer(cap int) *buffer {
  b := make(buffer, 0, cap)
  return &b
}

func (s *buffer) push(b byte) {
  *s = append(*s, b)
}

func (s *buffer) pop() {
	if len(*s) > 0 {
		*s = (*s)[:len(*s)-1]
	}
}

func (s *buffer) dup() {
	*s = append(*s, (*s)...)
}

func (s *buffer) rev() {
  t := *s
  n := len(t)

	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		t[i], t[j] = t[j], t[i]
	}
}

func (s *buffer) out() string {
  return string(*s)
}