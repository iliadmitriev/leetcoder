const MOD = int(1e9) + 7

func kInversePairs(n int, k int) int {

    // dp[0] - prev
    // dp[1] - current
    dp := [2][]int{
        make([]int, k + 1),
        make([]int, k + 1),
    }
    dp[0][0] = 1

    for i := 1; i <= n; i++ {
        window := 0
        for j := 0; j <= k; j++ {
            if j - i >= 0 {
                window -= dp[(i - 1) % 2][j - i]
            }
            window += dp[(i - 1) % 2][j]
            dp[i % 2][j] = window % MOD
        }
    }

    return dp[n % 2][k]
}