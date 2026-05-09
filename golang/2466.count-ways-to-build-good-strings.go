const MOD int = 1e9 + 7;

func countGoodStrings(low int, high int, zero int, one int) int {
    dp := make([]int, high + 2)

    for i := high; i >= 0; i-- {
        dp[i] = (b2i(i >= low) + dp[min(high + 1, i + one)] + dp[min(high + 1, i + zero)]) % MOD
    }

    return dp[0]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func b2i(x bool) int {
    if x {
        return 1
    }
    return 0
}