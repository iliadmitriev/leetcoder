func maxRepeating(sequence string, word string) int {
	n, m := len(sequence), len(word)
	dp := make([]int, n+1)
	maxRepeat := 0

	for i := m; i <= n; i++ {
		if sequence[i-m:i] == word {
			dp[i] = dp[i-m] + 1
			maxRepeat = max(maxRepeat, dp[i])
		}
	}

	return maxRepeat
}
