func stoneGameVIII(stones []int) int {
  n := len(stones)
  for i := 1; i < n; i++ {
    stones[i] += stones[i - 1]
  }

  dp := make([]int, n)
  dp[n - 1] = stones[n - 1] // -inf

  for i := n - 2; i > 0; i-- {
    dp[i] = max(dp[i + 1], stones[i] - dp[i + 1])
  }

  return dp[1] // should take at least 1
}