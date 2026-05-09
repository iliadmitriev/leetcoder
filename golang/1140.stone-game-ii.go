import (
    "math"
)

func stoneGameII(piles []int) int {
    n := len(piles)
    // accumulated piles of stone (prefix sum)
    acc := make([]int, n + 1)
    for i := 1; i <= n; i++ {
        acc[i] = acc[i - 1] + piles[i - 1]
    }

    // dp[pos][m]
    dp := make([][]int, n + 1)
    for i := range dp {
        dp[i] = make([]int, n + 1)
        for j := range dp[i] {
            dp[i][j] =  math.MinInt / 2
        }
    }

    for pos := n; pos >= 0; pos-- {
        for m := n; m >= 0; m-- {
            if pos + 2 * m >= n {
                // player can take rest of piles
                dp[pos][m] = acc[n] - acc[pos]
            } else {
                for step := 1; step <= 2 * m; step++ {
                    dp[pos][m] = max(
                        dp[pos][m],
                        acc[pos + step] - acc[pos] - dp[pos + step][max(m, step)],
                    )
                }
            }
        }
    }
    return (acc[n] + dp[0][1]) / 2
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}