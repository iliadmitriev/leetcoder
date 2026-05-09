func new21Game(n int, k int, maxPts int) float64 {
    // optimize 1
    if k == 0 {
        return 1.0
    }
    // optimize 2
    mPts := float64(maxPts)
    if k == 1 {
        return float64(min(maxPts, n)) / mPts
    }
    // optimize 3
    if k - 1 + maxPts <= n {
        return 1.0
    }

    // dp
    dp := make([]float64, n + maxPts)
    // base case
    for i := k; i <= n; i++ {
        dp[i] = 1.0
    }
    // base sum
    S := float64(min(n - k + 1, maxPts))

    for i := k - 1; i >= 0; i-- {
        dp[i] = S / mPts
        // add i-th element to sum, remove i+maxPts-th element from sum
        S += dp[i] - dp[i + maxPts]
    }
    return dp[0]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}