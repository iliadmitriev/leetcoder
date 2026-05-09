import (
	"strings"
)

type Deque struct {
	data  []int
	front int
	back  int
	size  int
}

func NewDeque(n int) *Deque {
	return &Deque{
		data:  make([]int, n),
		front: n / 2,
		back:  n/2 + 1,
		size:  n,
	}
}

func (d *Deque) PushFront(x int) {
	d.data[d.front] = x
	d.front = (d.front - 1 + d.size) % d.size
}

func (d *Deque) PopFront() int {
	d.front = (d.front + 1) % d.size
	x := d.data[d.front]
	return x
}

func (d *Deque) PushBack(x int) {
	d.data[d.back] = x
	d.back = (d.back + 1) % d.size
}

func (d *Deque) PopBack() int {
	d.back = (d.back - 1 + d.size) % d.size
	x := d.data[d.back]
	return x
}

func (d *Deque) Empty() bool {
	return d.front == (d.back-1+d.size)%d.size
}

func (d *Deque) Len() int {
	return (d.back - d.front - 1 + d.size) % d.size
}

func sortString(s string) string {
	N := 26
	base := 'a'
	q := NewDeque(N + 1)
	c := make([]int, N)
	res := strings.Builder{}

	for _, ch := range s {
		c[ch-base]++
	}

	for i := range N {
		if c[i] > 0 {
			q.PushBack(i)
		}
	}

	for !q.Empty() {
		for i := q.Len(); i > 0; i-- {
			ch := q.PopFront()
			res.WriteRune(base + rune(ch))
			c[ch]--

			if c[ch] > 0 {
				q.PushBack(ch)
			}
		}

		for i := q.Len(); i > 0; i-- {
			ch := q.PopBack()
			res.WriteRune(base + rune(ch))
			c[ch]--

			if c[ch] > 0 {
				q.PushFront(ch)
			}
		}
	}

	return res.String()
}
