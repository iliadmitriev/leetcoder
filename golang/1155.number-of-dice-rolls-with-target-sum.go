const MOD = int(1e9) + 7


func numRollsToTarget(n int, k int, target int) int {
    if n > target || n * k < target {
        return 0
    }

    dp := make([][]int, n + 1)
    for i := range dp {
        dp[i] = make([]int, target + 1)
    }
    dp[0][0] = 1

    for x := 1; x <= n; x++ {
        for t := target; t >= 0; t-- {
            for i := 1; i <= k; i++ {
                if t >= i {
                    dp[x][t] += dp[x - 1][t - i]
                    dp[x][t] %= MOD
                }
            }
        }
    }

    return dp[n][target]
}