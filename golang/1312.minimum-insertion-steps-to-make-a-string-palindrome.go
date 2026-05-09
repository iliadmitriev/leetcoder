func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func minInsertions(s string) int {
    n := len(s)
    // init 
    dp := make([][]int, n)
    for i := range dp {
        dp[i] = make([]int, n)
    }

    for win := 1; win < n; win++ {
        for l := 0; l < n - win; l++ {
            r := l + win
            if s[l] == s[r] {
                dp[l][r] = dp[l + 1][r - 1]
            } else {
                dp[l][r] = 1 + min(dp[l + 1][r], dp[l][r - 1])
            }
        }
    }

    return dp[0][n - 1]
}