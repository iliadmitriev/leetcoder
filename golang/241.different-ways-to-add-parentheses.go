func diffWaysToCompute(expression string) []int {
	if len(expression) == 0 {
		return []int{}
	}

	if len(expression) == 1 && '0' <= expression[0] && expression[0] <= '9' {
		return []int{int(expression[0] - '0')}
	}

	if len(expression) == 2 && '0' <= expression[0] && expression[0] <= '9' && '0' <= expression[1] && expression[1] <= '9' {
		return []int{int(expression[0]-'0')*10 + int(expression[1]-'0')}
	}

	result := make([]int, 0)
	for i := 0; i < len(expression); i++ {
		if '0' <= expression[i] && expression[i] <= '9' {
			continue
		}

		leftResult := diffWaysToCompute(expression[:i])
		rightResult := diffWaysToCompute(expression[i+1:])

		for _, left := range leftResult {
			for _, right := range rightResult {
				if expression[i] == '+' {
					result = append(result, left+right)
				} else if expression[i] == '-' {
					result = append(result, left-right)
				} else if expression[i] == '*' {
					result = append(result, left*right)
				}
			}
		}

	}

	return result
}
