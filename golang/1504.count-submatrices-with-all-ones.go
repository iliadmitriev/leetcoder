func numSubmat(mat [][]int) int {
	total := 0
	m, n := len(mat), len(mat[0])

	heights := make([]int, n)

	for i := range m {
		for j := range n {
			if mat[i][j] == 1 {
				heights[j]++
			} else {
				heights[j] = 0
			}
		}

		stack := -1
		dp := make([]int, n)

		for j := range n {
			for stack >= 0 && heights[stack] >= heights[j] {
				stack--
			}

			if stack == -1 {
				dp[j] = (j - stack) * heights[j]
			} else {
				dp[j] = dp[stack] + (j-stack)*heights[j]
			}

			stack = j
			total += dp[j]
		}

	}

	return total
}
