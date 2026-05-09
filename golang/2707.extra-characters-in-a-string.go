
func minExtraChar(s string, dictionary []string) int {
    n := len(s)
    dp := make([]int, n + 1)
    for i := range dp { dp[i] = n + 1 }
    dp[n] = 0

    // optimize 1: use uniq set of words with O(1) access
    // optimize 2: use uniq set of lengths instead of iterating 0 .. n
    lengths := make(map[int]bool)
    vocab := make(map[string]bool)
    for _, word := range dictionary {
        lengths[len(word)] = true
        vocab[word] = true
    }

    for pos := n - 1; pos >= 0; pos-- {
        for length := range lengths {
            if pos + length <= n && vocab[s[pos: pos + length]] {
                if dp[pos] > dp[pos + length] {
                    dp[pos] = dp[pos + length]
                }
            }
        }
        if dp[pos] > 1 + dp[pos + 1] {
            dp[pos] = 1 + dp[pos + 1]
        }
    }

    return dp[0]
}