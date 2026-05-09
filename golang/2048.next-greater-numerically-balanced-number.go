import (
	"math"
)

type BalancedNumber struct {
	bal []int
}

func NewBalancedNumber() *BalancedNumber {
	return &BalancedNumber{
		bal: make([]int, 0),
	}
}

func (b *BalancedNumber) Gen(n int) {
	var m int
	if n > 0 {
		m = int(math.Log10(float64(n)))
	}
	m++

	b.gen(0, 0, m, make([]int, 10))
	b.gen(0, 0, m+1, make([]int, 10))
}

func (b *BalancedNumber) isBalanced(voc []int) bool {
	for i := range 10 {
		if voc[i] == i || voc[i] == 0 {
			continue
		}
		return false
	}
	return true
}

func (b *BalancedNumber) gen(i, cur, m int, voc []int) {
	if i == m {
		if b.isBalanced(voc) {
			b.bal = append(b.bal, cur)
		}
		return
	}

	for d := 1; d <= m; d++ {
		if voc[d] == d || voc[d]+m-i < d {
			continue
		}

		voc[d]++
		b.gen(i+1, cur*10+d, m, voc)
		voc[d]--
	}
}

// Get returns the next greater numerically-balanced number using binary search with right bias
func (b *BalancedNumber) Get(n int) int {
	var mid int
	lo, hi := 0, len(b.bal)

	for lo < hi {
		mid = (lo + hi) / 2

		if b.bal[mid] > n {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return b.bal[lo]
}

func nextBeautifulNumber(n int) int {
	bal := NewBalancedNumber()
	bal.Gen(n)
	return bal.Get(n)
}
