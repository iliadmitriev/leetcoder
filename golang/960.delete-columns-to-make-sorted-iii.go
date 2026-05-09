
func minDeletionSize(strs []string) int {
	rows := len(strs)
	cols := len(strs[0])

	dp := make([]int, cols)
	for i := range dp {
		dp[i] = 1
	}

	removed := cols - 1 // worst case remove all but one

	for i := range cols {
		for j := range i {
			order := true

			for k := range rows {
				if strs[k][j] > strs[k][i] {
					order = false
					break
				}
			}

			if order {
				dp[i] = max(dp[i], dp[j]+1)
			}
		}

		removed = min(removed, cols-dp[i])
	}

	return removed
}
