
func maxCollectedFruits(fruits [][]int) int {
	n := len(fruits)
	total := 0

	for i := range n {
		total += fruits[i][i]
	}

	pre, cur := make([]int, n), make([]int, n)
	pre[n-1] = fruits[0][n-1]

	for i := 1; i < n-1; i++ {
		for j := max(i+1, n-1-i); j < n; j++ {
			cur[j] = pre[j]

			if j-1 >= 0 {
				cur[j] = max(cur[j], pre[j-1])
			}

			if j+1 < n {
				cur[j] = max(cur[j], pre[j+1])
			}

			cur[j] += fruits[i][j]
		}

		pre, cur = cur, pre
	}

	total += pre[n-1]

	pre, cur = make([]int, n), make([]int, n)
	pre[n-1] = fruits[n-1][0]

	for i := 1; i < n-1; i++ {
		for j := max(i+1, n-1-i); j < n; j++ {
			cur[j] = pre[j]

			if j-1 >= 0 {
				cur[j] = max(cur[j], pre[j-1])
			}

			if j+1 < n {
				cur[j] = max(cur[j], pre[j+1])
			}

			cur[j] += fruits[j][i]
		}

		pre, cur = cur, pre
	}

	total += pre[n-1]

	return total
}
