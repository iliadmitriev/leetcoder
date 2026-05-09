const MOD = int(1e9) + 7

func numWays(steps int, arrLen int) int {
    arrLen = min(steps / 2 + 1, arrLen)
    dp := make([][]int, steps + 1)
    for i := 0; i <= steps; i++ { dp[i] = make([]int, arrLen) }

    // base case
    dp[0][0] = 1

    for step := 1; step <= steps; step++ {
        for pos := arrLen - 1; pos >= 0; pos-- {
            dp[step][pos] = dp[step - 1][pos]
            if pos > 0 {
                dp[step][pos] += dp[step - 1][pos - 1]
            }
            if pos < arrLen - 1 {
                dp[step][pos] += dp[step - 1][pos + 1]
            }
            dp[step][pos] %= MOD
        }
    }
    return dp[steps][0]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}