
type Stack []int

func (s *Stack) Empty() bool {
	return len(*s) == 0
}

func (s *Stack) Top() int {
	return (*s)[len(*s)-1]
}

func (s *Stack) Push(x int) {
	(*s) = append((*s), x)
}

func (s *Stack) Pop() int {
	x := (*s)[len(*s)-1]
	(*s) = (*s)[:len(*s)-1]
	return x
}

func NewStack(size int) *Stack {
	st := make(Stack, 0, size)
	return &st
}

func finalPrices(prices []int) []int {
	pricesWithDiscount := make([]int, len(prices))
	copy(pricesWithDiscount, prices)

	st := NewStack(len(prices))
	for i, price := range prices {
		for !st.Empty() && pricesWithDiscount[st.Top()] >= price {
			pricesWithDiscount[st.Top()] -= price
			st.Pop()
		}

		st.Push(i)
	}

	return pricesWithDiscount
}
