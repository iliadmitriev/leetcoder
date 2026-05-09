func paintWalls(cost []int, time []int) int {
    n := len(cost)
    // dp[i][left] - min cost of paint starting from i, with left unpainted walls
    dp := make([][]int, n + 1)
    INF := int(1e10)
    for i := range dp {
        dp[i] = make([]int, n + 1)
        for j := range dp[i] {
            dp[i][j] = INF
        }
    }

    // base case: if there is no unpainted walls left == 0
    for i := n; i >= 0; i-- {
        dp[i][0] = 0
    }

    for i := n - 1; i >= 0; i-- {
        for left := 1; left <= n; left++ {
            dp[i][left] = min(
                cost[i] + dp[i + 1][max(0, left - 1 - time[i])],
                dp[i + 1][left],
            )
        }
    }

    return dp[0][n]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}