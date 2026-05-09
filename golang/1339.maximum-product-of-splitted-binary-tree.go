
type SumTree struct {
	sums []int
}

func (s *SumTree) calculate(node *TreeNode) int {
	if node == nil {
		return 0
	}

	left := s.calculate(node.Left)
	right := s.calculate(node.Right)
	res := node.Val + left + right

	s.sums = append(s.sums, res)

	return res
}

func maxProduct(root *TreeNode) int {
	tree := SumTree{}
	tree.calculate(root)

	sums := tree.sums
	total := sums[len(sums)-1]

	maxProd := 0

	for _, sum := range sums {
		maxProd = max(maxProd, sum*(total-sum))
	}

	return maxProd % int(1e9+7)
}
