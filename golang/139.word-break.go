
func wordBreak(s string, wordDict []string) bool {
	n := len(s)
	dp := make([]bool, n+1)
	dp[n] = true

	words := make(map[string]bool, n)
	for i := range wordDict {
		words[wordDict[i]] = true
	}

	for i := n - 1; i >= 0; i-- {
		for j := i; j <= n; j++ {
			if dp[j] && words[s[i:j]] {
				dp[i] = dp[j]
				break
			}
		}
	}

	return dp[0]
}
