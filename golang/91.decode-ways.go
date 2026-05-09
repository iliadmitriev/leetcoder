func numDecodings(s string) int {
    n := len(s)
    dp := make([]int, n + 1)
    dp[n] = 1

    for i := n - 1; i >= 0; i-- {
        if s[i] == '0' {
            continue
        }

        dp[i] += dp[i + 1]

        if i < n - 1 && "10" <= s[i: i + 2] && s[i: i + 2] <= "26" {
            dp[i] += dp[i + 2]
        }
    }

    return dp[0]
}