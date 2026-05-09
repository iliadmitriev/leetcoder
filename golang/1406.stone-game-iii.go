func stoneGameIII(stoneValue []int) string {
    n := len(stoneValue)
    // accumulated array, starting from 0
    acc := make([]int, n + 1)
    for i := 1; i <= n; i++ {
        acc[i] = acc[i - 1] + stoneValue[i - 1]
    }

    // bottom up dp
    dp := make([]int, n + 1)
    for pos := n; pos >= 0; pos-- {
        dp[pos] = max(
            acc[min(n, pos + 1)] - acc[pos] - dp[min(n, pos + 1)],
            acc[min(n, pos + 2)] - acc[pos] - dp[min(n, pos + 2)],
            acc[min(n, pos + 3)] - acc[pos] - dp[min(n, pos + 3)],
        )
    }
    if dp[0] > 0 {
        return "Alice"
    } else if dp[0] < 0 {
        return "Bob"
    }
    return "Tie"
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b, c int) int {
    if a > b {
        if a > c {
            return a
        }
        return c
    }
    if b > c {
        return b
    }
    return c
}