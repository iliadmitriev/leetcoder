
type IndexStack []int

func (h *IndexStack) Push(x int) { *h = append(*h, x) }
func (h *IndexStack) Pop() int {
	x := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return x
}

func (h *IndexStack) IsEmpty() bool {
	return len(*h) == 0
}

type CharMapVector []IndexStack

func (m *CharMapVector) Get(ch byte) *IndexStack {
	return &(*m)[ch-'a']
}

func (m *CharMapVector) GetMin() *IndexStack {
	c := 0
	for ; c < 26; c++ {
		if len((*m)[c]) > 0 {
			break
		}
	}

	return &(*m)[c]
}

func NewCharMapVector() CharMapVector {
	return make(CharMapVector, 26)
}

func clearStars(s string) string {
	tmp := []byte(s)
	indices := NewCharMapVector()

	for i, c := range tmp {
		if c != '*' {
			indices.Get(c).Push(i)
			continue
		}

		j := indices.GetMin().Pop()
		tmp[j] = '*'
	}

	res := make([]byte, 0, len(tmp))
	for i := range tmp {
		if tmp[i] != '*' {
			res = append(res, tmp[i])
		}
	}
	return string(res)
}
