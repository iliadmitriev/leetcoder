
type runeStack []rune

func (s *runeStack) push(ch rune) {
	*s = append(*s, ch)
}

func (s *runeStack) pop() rune {
	x := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return x
}

func (s *runeStack) top() rune {
	return (*s)[len(*s)-1]
}

func (s *runeStack) isEmpty() bool {
	return len(*s) == 0
}

func (s *runeStack) String() string {
	return string(*s)
}

func NewRuneStack(reserve int) *runeStack {
	st := make(runeStack, 0, reserve)
	return &st
}

func clearDigits(s string) string {
	res := NewRuneStack(len(s))

	for _, ch := range s {

		if unicode.IsLetter(ch) {
			res.push(ch)
			continue
		}

		if !res.isEmpty() && unicode.IsLetter(res.top()) {
			res.pop()
		} else {
			res.push(ch)
		}

	}

	return res.String()
}
