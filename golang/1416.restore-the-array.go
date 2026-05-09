const MOD int = 1e9 + 7


func numberOfArrays(s string, k int) int {
    n := len(s)
    dp := make([]int, n + 1)
    dp[n] = 1

    for i := n - 1; i >= 0; i-- {
        val := int(s[i] - '0')

        if val == 0 {
            continue
        }
        
        for j := i + 1; val <= k && j <= n; j++ {
            dp[i] = (dp[i] + dp[j]) % MOD
            if j < n {
                val = val * 10 + int(s[j] - '0')
            }
        }
    }
    
    return dp[0]
}