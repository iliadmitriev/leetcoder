func calculateTax(brackets [][]int, income int) float64 {
	tax := 0.0
	prev := 0

	for i := 0; i < len(brackets) && income > 0; i++ {
		base := min(income, brackets[i][0]-prev)

		tax += float64(base) * float64(brackets[i][1]) / 100.0
		income -= base

		prev = brackets[i][0]
	}

	return tax
}
